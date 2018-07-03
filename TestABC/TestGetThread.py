import threading,shutil,time
# i =0
# threads =[]
# # print('C:\\Users\\sl\\Documents\\Tencent Files\\629943345\\FileRecv\\LongTimeOnlineDump\\TestABC\\test'+str(i)+'.txt')
# def RECVideo():
#     global i
#     while True:
#
#         shutil.copyfile('c:\\test.txt','C:\\Users\\sl\\Documents\\Tencent Files\\629943345\\FileRecv\\LongTimeOnlineDump\\TestABC\\test'+str(i)+'.txt')
#         i= i+1
#         time.sleep(5)
# t2 = threading.Thread(target=RECVideo,args=())
# t2.start()
# threads.append(t2)
# for t in threads:
#     t.join(0.01)
# exit()
result=[['/usr/local/arcvideo/live/tmpdir/27875_2703229339038531_transcoder_task.xml', ['http://172.17.230.227:8080/5jziwi9a/live/hls/2055b17d79804b9580eca5619bc689d4/', 'http://172.17.230.227:8080/5jziwi9a/live/hls/2055b17d79804b9580eca5619bc689d7/', 'http://172.17.230.227:8080/5jziwi9a/live/hls/2055b17d79804b9580eca5619bc689d0/', 'http://source.test:9011//live/ffecdc17bdab4045ba98b088810486e5/'], ['rtmp://172.17.230.227/live/5jziwi9a_HOdiOHBY', 'rtmp://172.17.230.65:1935/live/MHp0chBp']], ['/usr/local/arcvideo/live/tmpdir/24273_1469799459488684_transcoder_task.xml', ['http://172.17.230.227:8080/5jziwi9a/live/hls/2055b17d79804b9580eca5619bc689d4/', 'http://172.17.230.227:8080/5jziwi9a/live/hls/2055b17d79804b9580eca5619bc689d7/', 'http://172.17.230.227:8080/5jziwi9a/live/hls/2055b17d79804b9580eca5619bc689d0/', 'http://source.test:9011//live/ffecdc17bdab4045ba98b088810486e5/'], ['rtmp://172.17.230.227/live/5jziwi9a_HOdiOHBY', 'rtmp://172.17.230.65:1935/live/MHp0chBp']]]
for numb in range(len(result)):
    print(result[numb][0])