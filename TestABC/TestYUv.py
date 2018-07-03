
import time
# r= '/mnt/data/local-disk2-ssd/pid9999_output_44028624_0.ts'
# dat = '111'
# di={'pid':'2'}
# print('/mnt/data/remote/liveData/longTimeTest/'+dat+'/'+di['pid'])
# print(r.replace('/mnt/data/local-disk2-ssd/','/mnt/data/remote/liveData/longTimeTest/111/2'))
dat=''
def TestF():
    global dat
    dat = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # print('dar1',dat)
def TestE():
    TestF()
    print('dar',dat)
if __name__ == '__main__':
    while True:
        TestE()
        time.sleep(60)