import logging
import functools
import os
import time
from logging.handlers import RotatingFileHandler
from config import Log_level, Log_path

class LogCollection:
    def __init__(self):
        if not os.path.exists(Log_path):
            os.makedirs(Log_path)
        self.filename=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) + '.log'
        self.log = logging.getLogger('mylogger')
        self.log.setLevel(Log_level)
        self.fh = logging.FileHandler(Log_path + self.filename)
        self.fh.setLevel(Log_level)
        self.fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s '
                                               '[%(pathname)s line:%(lineno)d][function:%(funcName)s] %(message)s'))
        self.sh = logging.StreamHandler()
        self.sh.setLevel(logging.INFO)
        self.sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.log.addHandler(self.fh)
        self.log.addHandler(self.sh)
        try:
            rtfHandler = RotatingFileHandler(
                Log_path +self.filename, maxBytes=100*1024*1024, backupCount=10)
        except :
            self.log.exception("Exception Logged")
        else:
            self.log.addHandler(rtfHandler)
    # 初始化日志

    def funlog(self, leavel, model):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, ** kargs):
                try:
                    result = func(*args, ** kargs)
                except:
                    self.log.exception("Exception Logged")
                    raise
                if model == "input":
                    leavel('Start %s(%s, %s)' % (func.__name__, args, kargs))
                elif model == "output":
                    leavel('Start %s: %s' % (func.__name__, func(*args, ** kargs)))
                elif model == "all":
                    leavel('Start  %s(%s, %s): %s' % (func.__name__, args, kargs, result))
                else:
                    leavel('Start %s' % func.__name__)
                return result
            return wrapper
        return decorator
    # 打印函数调用日志的装饰器，输入参数level表示日志等级如logging.debug, ），model表示打印日志模式（all，函数输出输入都打印，input，打印入参，out打印函数返回值）
