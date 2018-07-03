# from apscheduler.schedulers.blocking import BlockingScheduler
# from datetime import datetime
# import time
# def tick():
#     print('Tick! The time is: %s' % datetime.now())
#     while True:
#         # time.sleep(3)
#         print("11111")
# def run():
#     #调用了 APScheduler 模块
#     scheduler = BlockingScheduler()
#     scheduler.add_job(tick,'interval',seconds=3) #tick也可以传参数，3秒执行tick函数
#     try:
#         scheduler.start()
#     except (KeyboardInterrupt, SystemExit):
#         scheduler.shutdown()
# run()
# import time,datetime
# def doSth():
#
#     print('test')
#
#     # 假装做这件事情需要一分钟
#
#     time.sleep(60)
#     print('test2')
#
#
# def main(h=15 ,m=29):
#
#     '''h表示设定的小时，m为设定的分钟'''
#
#     while True:
#
#         # 判断是否达到设定时间，例如0:00
#
#         while True:
#
#             now = datetime.datetime.now()
#
#             # 到达设定时间，结束内循环
#
#             if now.hour==h and now.minute==m:
#
#                 break
#
#             # 不到时间就等20秒之后再次检测
#
#             time.sleep(20)
#
#         # 做正事，一天做一次
#
#         doSth()
#
#
#
# main()
b =b'File: \\172.17.228.6\\LiveData\\longTimeTest\\20180621\\82_1135277886193223_transcoder_task.xml\\pid19805_srcdump_0x1b14810_0x0_udp___239.4.4.24_8888_1_20180621.ts ,Total number of errors in this file:0 ,taskId:00000164206045cb610c22b200ac001100e600ca\nFile: \\172.17.228.6\\LiveData\\longTimeTest\\20180621\\82_1135277886193223_transcoder_task.xml\\pid19805_srcdump_0x1b14810_0x0_udp___239.4.4.24_8888_1_20180621.ts ,Total number of warnings in this file:0 ,taskId:00000164206045cb610c22b200ac001100e600ca\nFile: \\172.17.228.6\\LiveData\\longTimeTest\\20180621\\81_1134806457865380_transcoder_task.xml\\pid40374_srcdump_0xb85d40_0x0_udp___239.4.4.18_8888_0_20180621.ts ,Total number of errors in this file:0 ,taskId:0000016420604619efed0f5400ac001100e600ca\nFile: \\172.17.228.6\\LiveData\\longTimeTest\\20180621\\81_1134806457865380_transcoder_task.xml\\pid40374_srcdump_0xb85d40_0x0_udp___239.4.4.18_8888_0_20180621.ts ,Total number of warnings in this file:0 ,taskId:0000016420604619efed0f5400ac001100e600ca\n'
print(str(b,encoding='utf-8'))