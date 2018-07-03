#!/bin/bash
app_pid=`ps axu | grep trasncoder.py| grep -v grep | awk '{print $2}'`
kill $app_pid
sleep 3
re_checkpid=`ps axu | grep trasncoder.py| grep -v grep | awk '{print $2}'`
if [ $re_checkpid ];then
  echo "stop failed"
else
  echo "stop success"
fi