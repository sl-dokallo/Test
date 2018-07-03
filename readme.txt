项目背景：以往在线的源内容判断都是通过人工去检查，比较耗时，并且容易漏测；我们已具备离线文件的技审工具，可以通过在线源收录成离线文件然后取baton技审，技审结果邮件通知

运行脚本之前先安装环境 
1.上传python.zip到任意位置，解压zip包，执行install_python3
2.跳出install python3 complete和install python complete即安装成功

设置结果收件人
1.修改config.py中的receivers数组，在数组中添加完整的email地址，可以添加多个收件人

运行脚本
1.运行python3 transcoder.py 时:分:秒 每小时录制时间（比如8~18就是指在每时8分到18分录制输入输出源） ，设置了之后再设置的时间会把当天录制的结果上传到baton分析，结果发送邮件

录制下来的文件存放在\\172.17.228.6\LiveData\longtimeTest目录下

后台运行脚本
1.修改start.sh
vi start.sh
#!/bin/bash
python3 transcoder.py 时:分:秒 每小时录制时间
修改成需要的时间；默认为每天23点59分58秒上传录制文件到baton，每时8分到18分录制输入源

后台停止脚本
1.运行stop.sh