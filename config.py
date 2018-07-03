#coding:utf-8
import logging, os

Log_level = logging.INFO   # 设置日志等级，CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
Log_path = os.path.abspath(os.path.dirname(__file__)) +"/logs/"   #日志路径，默认设置为当前路径+log,其他路径示例Log_path = "/mnt/data/local-disk1/xltest/logs/"
# 第三方 SMTP 服务
mail_host = "smtp.163.com"      # SMTP服务器
mail_user = "shenlei1994131@163.com"                  # 用户名
mail_pass = "629943345"               # 授权密码，非登录密码

sender = 'shenlei1994131@163.com'
# 发件人邮箱(最好写全, 不然会失败)
receivers = ['sl@arcvideo.com']