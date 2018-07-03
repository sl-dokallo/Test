import subprocess,threading,time,os,shlex,multiprocessing,datetime
from tools.eamil.sendEmail import sendEmail
checkVideoResult = []
dat = '20180621'
threads = []
chklist =[]
# def checkResult():
#     global chk
#     global chklist
#     for cv in checkVideoResult:
#         chk = cv.stdout.readline()
#         print(chk)
#         if b' Total number of warnings in this file' in  chk or b' Total number of errors in this file' in chk:
#             print(str(chk,encoding='utf-8'))
#             chklist.append(str(chk,encoding='utf-8'))
#     return chklist
def videoCheck():
    result = []
    # os.chdir(')
    cmd = 'python ./tools/baton/verifyfile.py '+'/mnt/data/remote/liveData/longTimeTest/'+dat
    # print(cmd)
    outMeessage = subprocess.Popen(str(cmd),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    outMeessage = outMeessage.stdout.read()
    outMeessage = str(outMeessage,encoding='utf-8')
    print(outMeessage)
    sendEmail(outMeessage,dat+'结果')
    # sendEmail(outMeessage,dat+'结果')
    # checkVideoResult.append(outMeessage)
    # pool = multiprocessing.Pool(processes=1)
    # result.append(pool.apply_async(checkResult, ()))
    # for r in result:
    #     print(r.get())
    # pool.close()
    # pool.join()
    # t1 = threading.Thread(target=checkResult,args=())
    #
    # # print(chklist)
    # # startTime = time.time()
    # threads.append(t1)
    # t1.setDaemon(True)
    # t1.start()
    # time.sleep(600)
    # for t in threads:
    #     t.join(0.01)
    # exit()
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
    t2 = threading.Thread(target=fixedTime,args=(11,30,32))
    t2.start()
    # videoCheck()