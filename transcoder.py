import subprocess,shlex
# from datetime import datetime
import time,datetime
import threading,shutil,shlex
from tools.log.logcon import log
from tools.eamil.sendEmail import *
# from lxml.etree import XMLSyntaxError
from lxml import etree
# from tools.baton.verifyfile import *
# dat = time.strftime("%Y%m%d%H%M%S", time.localtime())
checkVideoResult = []
file_path = os.path.dirname(os.path.realpath(__file__))#脚本当前路径
dat =''
try:
    os.mkdir('/mnt/data/remote/liveData')
    cmd = 'mount //172.17.228.6/LiveData /mnt/data/remote/liveData/ -o user=user,password=user'
    subprocess.Popen(shlex.split(cmd),stdin=subprocess.PIPE,stdout=subprocess.PIPE)
except:
    log.exception("Exception Logged")
# time.sleep(60)
try:
    os.chdir('/mnt/data/remote/liveData/longTimeTest')
except:
    log.info("请检查挂载")
    log.exception("Exception Logged")
# time.sleep(60)



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
    global dat
    dat = time.strftime("%Y%m%d", time.localtime())
    os.chdir('/mnt/data/remote/liveData/longTimeTest/')
    try:
        os.mkdir(dat)
    except:
        pass
    # V=0
    # buf2 = ''
    #遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)

    for fi in files:
        TargetPath = []
        URI = []
        fi_d = os.path.join(filepath,fi)
        # if os.path.isdir(fi_d):
        #     getpath(fi_d,result)
        #
        # else:
        if '.xml' in fi_d:
            try:

                os.chdir('/mnt/data/remote/liveData/longTimeTest/'+dat)
                os.mkdir(fi_d.split('/')[-1])
            except :
                pass

            tree = etree.parse(fi_d, etree.XMLParser(ns_clean=True, recover=True))
            # trees = DOMTree.documentElement
            for r in tree.xpath('//OutputGroups/OutputGroup/TargetPath'):
                TargetPath.append(r.text)
            for r in tree.xpath('//Inputs/Input/URI'):
                URI.append(r.text)
            result.append([fi_d,TargetPath,URI])
        elif 'ts' in fi_d or 'txt' in fi_d:
            result.append(fi_d)
        # elif 'ts' in fi_d:
        #     result.append(fi_d)

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
                    cmd = './rtmpdump -r '+r+' -o '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[numb][0].split('/')[-1],r1.replace('rtmp://','').replace('/','-').replace('/','-').replace(':','-').replace('\\','-').replace('*','-').replace('?','-').replace('"','-').replace('<','-').replace('>','-').replace('|','-').replace(' ','')+'.flv')
                    subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    cmd1 = 'ps -ef | grep '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[numb][0].split('/')[-1],r1.replace('rtmp://','').replace('/','-').replace(':','-').replace('\\','-').replace('*','-').replace('?','-').replace('"','-').replace('<','-').replace('>','-').replace('|','-').replace(' ','')+'.flv')+' | grep -v grep | cut -c 9-15 | xargs'
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
                    cmd = './rtmpdump -r '+r1+' -o '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[numb][0].split('/')[-1],r1.replace('rtmp://','').replace('/','-').replace(':','-').replace('\\','-').replace('*','-').replace('?','-').replace('"','-').replace('<','-').replace('>','-').replace('|','-').replace(' ','')+'.flv')
                    cmd1 = 'ps -ef | grep '+os.path.join('/mnt/data/remote/liveData/longTimeTest/',dat,result[numb][0].split('/')[-1],r1.replace('rtmp://','').replace('/','-').replace(':','-').replace('\\','-').replace('*','-').replace('?','-').replace('"','-').replace('<','-').replace('>','-').replace('|','')+'.flv')+' | grep -v grep | cut -c 9-15 | xargs'
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
            time.sleep(1)
            t2 = threading.Thread(target=RECVideo,args=(transcodeTasks[0],di))
            t2.start()
            # fixedTime(15,40,37)
            # t2.setDaemon(True)
            # threads.append(t2)
        # if task_failed or performance_not_ok :
        #     sendEmail('在'+result[V]+'任务存在异常，错误码为:'+buf2,'任务异常')
        #     break



            # for t in threads:
            #     t.join(0.01)
            # exit()
        else:
            continue

def RECVideo(pid,di):
    res = getpath('/mnt/data/local-disk2-ssd/',[])
    while True:
        for r in res:
            if '.ts' in r:
                if pid in r and '_0.ts' in r:
                    fsize = os.path.getsize(r)
                    if fsize > 450000000:
                        # print('R:',r)
                        # print('W',r.replace('/mnt/data/local-disk2-ssd/','/mnt/data/remote/liveData/longTimeTest/'+dat+'/'+di[pid].split('/')[-1]).replace('.ts',dat+'.ts').replace('xmlpid','xml/pid'))
                        shutil.copy2(r,r.replace('/mnt/data/local-disk2-ssd/','/mnt/data/remote/liveData/longTimeTest/'+dat+'/'+di[pid].split('/')[-1]).replace('.ts','_'+dat+'.ts').replace('xmlpid','xml/pid'))
                if pid in r and '_1.ts' in r:
                    fsize = os.path.getsize(r)
                    if fsize > 450000000:
                        shutil.copy2(r,r.replace('/mnt/data/local-disk2-ssd/','/mnt/data/remote/liveData/longTimeTest/'+dat+'/'+di[pid].split('/')[-1]).replace('.ts','_'+dat+'.ts').replace('xmlpid','xml/pid'))
                # shutil.
        time.sleep(1)
def videoCheck():
    # global dat

    dat = time.strftime("%Y%m%d", time.localtime())
    cmd = 'python '+file_path+'/tools/baton/verifyfile.py '+'/mnt/data/remote/liveData/longTimeTest/'+dat
    log.info('cmd:'+cmd)
    outMeessage = subprocess.Popen(str(cmd),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    outMeessage = outMeessage.stdout.read()
    outMeessage = str(outMeessage,encoding='utf-8')
    # print(outMeessage.stdout.read())
    # outMeessage = str(outMeessage.stdout.read(),encoding='utf-8')
    log.info('baton result:'+outMeessage)
    sendEmail(file_path,outMeessage,dat+'结果')
    # checkVideoResult.append(outMeessage)
    # t1 = threading.Thread(target=checkResult,args=())
    # # startTime = time.time()
    # threads.append(t1)
    # t1.setDaemon(True)

def fixedTime(h,m,s):
    # r =[]
    # result = getpath(sys.argv[1],[])
    # for r1 in result:
    #     r.append(r1.replace(r1.split(r1.split('/')[-1]))[0],'/mnt/data/remote/liveData/longTimeTestlongTimeTest'+r1.split(r1.split('/')[-1])+'/'+dat)
    '''h表示设定的小时，m为设定的分钟'''

    while True:

        # 判断是否达到设定时间，例如0:00

        while True:

            now = datetime.datetime.now()
            if now.hour==h and now.minute==m and now.second == s :
                videoCheck()
                break

if __name__ == '__main__':
    import sys
    a = sys.argv[1].split(':')
    t2 = threading.Thread(target=fixedTime,args=(int(a[0]),int(a[1]),int(a[2])))
    t2.start()
    # fixedTime(15,40,37)
    b = sys.argv[2].split('~')
    # c = sys.argv[3].split(':')
    while True:
        now = datetime.datetime.now()

        if  now.minute> int(b[0]) and now.minute < int(b[1]):
            transcoder()
        elif now.minute > int(b[1]):
            cmd = 'ps -ef | grep rtmpdump | grep -v grep | cut -c 9-15 | xargs kill -s 9'
            try:
                subprocess.Popen(str(cmd),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
                res = getpath('/mnt/data/local-disk2-ssd/',[])
                # print(res)
                for i in res:
                    if 'txt' in i:
                        os.remove(i)
            except:
                pass



