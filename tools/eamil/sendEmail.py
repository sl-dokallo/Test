import smtplib,os,time
from email.header import Header
from email.mime.text import MIMEText
from config import *
from tools.log.logcon import log
# # 第三方 SMTP 服务
# mail_host = "smtp.163.com"      # SMTP服务器
# mail_user = "shenlei1994131@163.com"                  # 用户名
# mail_pass = "629943345"               # 授权密码，非登录密码
#
# sender = 'shenlei1994131@163.com'
# # 发件人邮箱(最好写全, 不然会失败)
# receivers = ['sl@arcvideo.com']
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# content = '我用Python'
#
# title = '人生苦短'
# 邮件主题
dat = time.strftime("%Y%m%d", time.localtime())
def alter(file_path,file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file_path+'/tools/eamil/'+dat+'.html',"w",encoding="utf-8") as f:
        f.write(file_data)

# alter("file1", "09876", "python")

def sendEmail(file_path,content,title):

    content = content.replace(' taskId:','<tr><td>').replace(' ,Total number of warnings in this file:','</td><td>').replace(' ,Total number of errors in this file:','</td><td>').replace('\n','</td></tr>').replace(' ,File: ','</td><td>')
    alter(file_path,file_path+'/tools/eamil/Test.html','<tr><td></td></tr>',content)
    f = open(file_path+'/tools/eamil/'+dat+'.html', 'rb')
    mail_body = f.read()
    f.close()

    # content.split('')
    message = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:

        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        log.info("mail has been send successfully.")
    except smtplib.SMTPException as e:
        log.exception("Exception Logged")
    os.remove(file_path+'/tools/eamil/'+dat+'.html')
# def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
#     email_client = smtplib.SMTP(SMTP_host)
#     email_client.login(from_account, from_passwd)
#     # create msg
#     msg = MIMEText(content, 'plain', 'utf-8')
#     msg['Subject'] = Header(subject, 'utf-8')  # subject
#     msg['From'] = from_account
#     msg['To'] = to_account
#     email_client.sendmail(from_account, to_account, msg.as_string())
#
#     email_client.quit()

# if __name__ == '__main__':
#     content=' taskId:0000016420b739e0b9489cca00ac001100e600ca ,Total number of errors in this file:0 ,Total number of warnings in this file:0,File:\\\\172.17.228.6\\LiveData\\longTimeTest\\20180621\\82_1135277886193223_transcoder_task.xml\pid19805_srcdump_0x1b14810_0x0_udp___239.4.4.24_8888_1_20180621.ts\n taskId:0000016420b739e0b9489cca00ac001100e600ca ,Total number of errors in this file:0 ,Total number of warnings in this file:0,File:\172.17.228.6\LiveData\longTimeTest\20180621\82_1135277886193223_transcoder_task.xml\pid19805_srcdump_0x1b14810_0x0_udp___239.4.4.24_8888_1_20180621.ts\n taskId:0000016420b739e0b9489cca00ac001100e600ca ,Total number of errors in this file:0 ,Total number of warnings in this file:0,File:\\\\172.17.228.6\LiveData\longTimeTest\20180621\82_1135277886193223_transcoder_task.xml\pid19805_srcdump_0x1b14810_0x0_udp___239.4.4.24_8888_1_20180621.ts\n '
#     content = content.replace(' taskId:','<tr><td>')
#     content=content.replace(' ,Total number of warnings in this file:','</td><td>')
#     content=content.replace(' ,Total number of errors in this file:','</td><td>')
#     content=content.replace('\n','</td></tr>')
#     content=content.replace(',File:','</td><td>')
#     alter('C:\\Users\\sl\\Documents\\Tencent Files\\629943345\\FileRecv\\LongTimeOnlineDump\\Test.html','<tr><td></td></tr>',content)
    # sendEmail('<table border=1><tr><th>baton taskid</th><th>file Addree</th><th>wrong</th><th>error</th></tr></thead><tbody><tr><td>111</td><td>222</td><td>111</td><td>111</td></tr></tbody></table>','title')