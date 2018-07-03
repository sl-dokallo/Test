#!/bin/bash
python3 transcoder.py 23:59:58 14~19
sleep 3
re_checkpid=`ps axu | grep trasncoder.py| grep -v grep | awk '{print $2}'`
if [ $re_checkpid ];then
  echo "start success"
else
  echo "start fail"
fi