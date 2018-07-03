import subprocess,shlex
from datetime import datetime
import xml.dom.minidom,time
from os import open
import sys,threading,shutil,shlex
from tools.log.logcon import loger,log
from tools.eamil.sendEmail import *
# from lxml.etree import XMLSyntaxError
from lxml import etree
# from tools.baton.verifyfile import *
dat = time.strftime("%Y%m%d%H%M%S", time.localtime())
checkVideoResult = []
os.chdir('/mnt/data/remote/liveData/longTimeTest/')
os.mkdir(dat)
# file_path = os.path.dirname(os.path.realpath(__file__))#脚本当前路径
# def checkResult():
#     global chk
#     global chklist
#     for cv in checkVideoResult:
#         chk = cv.stdout.readline()
#         if b' Total number of warnings in this file' in  chk or b' Total number of errors in this file' in chk:
#             chklist.append(str(chk,encoding='utf-8'))

# def checkTxd(v):
#     global performance_not_ok
#     global task_failed
#     global buf2
#     global V
#     #log.info 'checktxd thread :' + str(v)
#     while True:
#         # log.info('v:',v)
#         try:
#             buf = txds[v].stdout.readline()
#             # print(buf)
#         except:
#             log.exception("Exception Logged")
#         # log.debug('buf:'+buf)
#         if buf == b'' and subprocess.Popen.poll(txds[v]) == None:
#             # log.info('1:')
#             task_failed = 1
#             break
#         if b"__WARNING__$[0x2100e]" in buf or b"__WARNING__$[0x2500b]" in buf or b'__ERROR__$[0x' in buf:
#             log.info('buf:'+buf2)
#             buf2 = str(buf,encoding='utf-8')
#             V=v
#             performance_not_ok = 1
#             # log.info('2')
#             break
#         # log.info()
#         if subprocess.Popen.poll(txds[v]) == 0: #//exit
#             break;
def getpath(filepath,result):

    # V=0
    # buf2 = ''
    #遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)

    for fi in files:
        TargetPath = []
        URI = []
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            getpath(fi_d,result)

        else:
            if '.xml' in fi_d:
                try:

                    os.chdir('/mnt/data/remote/liveData/longTimeTest/'+dat)
                    os.mkdir(fi_d.split('/')[-1])
                except :
                    log.exception("Exception Logged")

                tree = etree.parse(fi_d, etree.XMLParser(ns_clean=True, recover=True))
                # trees = DOMTree.documentElement
                for r in tree.xpath('//OutputGroups/OutputGroup/TargetPath'):
                    TargetPath.append(r.text)
                for r in tree.xpath('//Inputs/Input/URI'):
                    URI.append(r.text)
                result.append([fi_d,TargetPath,URI])
            elif 'ts' in fi_d:
                result.append(fi_d)
    return result
def transcoder():
    # performance_not_ok = 0
    # V=0
    # buf2 = ''
    # task_failed = 0
    di={}

    result = getpath('/usr/local/arcvideo/live/tmpdir',[])
    # print(result)
    # while True:
    for numb in range(len(result)):

        os.chdir('/usr/local/arcvideo/live/transcoder/')
        cmd = 'ps -ef | grep '+result[numb][0]+' | grep -v grep | cut -c 9-15 | xargs'
        log.info('task:'+cmd)

        txd = subprocess.Popen(str(cmd),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        txd =txd.stdout.read().decode('ascii').replace('\n','')
        log.info('pid:'+txd)
        # print(txd.stdout.read().decode('ascii').replace('\n',''))
        # print(type(txd.stdout.read().decode('ascii')))
        if  txd != '':
            # print(txd)
            transcodeTasks = [txd]
            # print(transcodeTasks)
            # outMeessage = subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            di[transcodeTasks[0]] = result[numb][0]
            # txds.append(outMeessage)
            # t1 = threading.Thread(target=checkTxd,args=(numb,))
            # startTime = time.time()
            # threads.append(t1)
            # t1.setDaemon(True)
            # os.mkdir(os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[0].split('/')[-1]))
            # t1.start()
            for r in result[numb][1]:
                # print(r)
                if 'rtmp' in r :
                    os.chdir('/usr/local/arcvideo/live/transcoder/Tools/rtmpdump')
                    cmd = './rtmpdump -r '+r+' -o '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[numb][0].split('/')[-1],r1.replace('rtmp://','')+'.flv')
                    subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    cmd1 = 'ps -ef | grep '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[numb][0].split('/')[-1],r1.replace('rtmp://','').replace('/','-')+'.flv')+' | grep -v grep | cut -c 9-15 | xargs'
                    txd = subprocess.Popen(str(cmd1),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
                    txd =txd.stdout.read().decode('ascii').replace('\n','')
                    log.info(cmd)
                    if txd=='':
                        subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                # elif  'rtmp' in r:
                #     cmd = './ffmpeg -i'+r+'-acodec copy -vcodec copy -f flv -y '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[0].split('/')[-1],'test2.flv')
                #     subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                elif 'udp' in r or 'http:' in r:
                    # print('/mnt/data/local-disk2-ssd/'+str(outMeessage.pid)+'_o.txt')
                    try:
                        os.mknod('/mnt/data/local-disk2-ssd/'+str(transcodeTasks[0])+'_o.txt')
                    except :
                        pass
            for r1 in result[numb][2]:
                # print('r1:',r1)
                if 'rtmp' in r1 :
                    os.chdir('/usr/local/arcvideo/live/transcoder/Tools/rtmpdump')
                    cmd = './rtmpdump -r '+r1+' -o '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[numb][0].split('/')[-1],r1.replace('rtmp://','').replace('/','-')+'.flv')
                    cmd1 = 'ps -ef | grep '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[numb][0].split('/')[-1],r1.replace('rtmp://','').replace('/','-')+'.flv')+' | grep -v grep | cut -c 9-15 | xargs'
                    txd = subprocess.Popen(str(cmd1),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
                    txd =txd.stdout.read().decode('ascii').replace('\n','')
                    log.info(cmd)
                    if txd=='':
                        subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)

                # elif  'rtmp' in r1:
                #     cmd = './ffmpeg -i'+r1+'-acodec copy -vcodec copy -f flv -y '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[0].split('/')[-1],'test2.flv')
                #     o = subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                elif  'udp' in r1 or 'http:' in r1:
                    try:
                        os.mknod('/mnt/data/local-disk2-ssd/'+str(transcodeTasks[0])+'.txt')
                    except:
                        pass
            time.sleep(120)
            t2 = threading.Thread(target=RECVideo,args=(transcodeTasks[0],di))
            t2.start()
            # t2.setDaemon(True)
            # threads.append(t2)
        # if task_failed or performance_not_ok :
        #     sendEmail('在'+result[V]+'任务存在异常，错误码为:'+buf2,'任务异常')
        #     break
        else:
            break



    # for t in threads:
    #     t.join(0.01)
    # exit()

def RECVideo(pid,di):
    res = getpath('/mnt/data/local-disk2-ssd/',[])
    while True:
        for r in res:
            if pid in r:
                # print('R:',r)
                # print('W',r.replace('/mnt/data/local-disk2-ssd/','/mnt/data/remote/liveData/longTimeTest/'+dat+'/'+di[pid].split('/')[-1]).replace('.ts',dat+'.ts').replace('xmlpid','xml/pid'))
                shutil.copy(r,r.replace('/mnt/data/local-disk2-ssd/','/mnt/data/remote/liveData/longTimeTest/'+dat+'/'+di[pid].split('/')[-1]).replace('.ts','-'+dat+'.ts').replace('xmlpid','xml/pid'))
        time.sleep(60)
if __name__ == '__main__':
    while True:
        transcoder()