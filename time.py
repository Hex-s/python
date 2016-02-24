#!/usr/bin/python
#-*- coding:utf-8 -*-

import time

#自1970-1-1 00:00:00至今的毫秒数
ticks = time.time()
#print('since 1970-1-1:',ticks)

#获取当前时间
localtime = time.localtime(time.time())
#print(localtime)
#Local current time : time.struct_time(tm_year=2013, tm_mon=7, 
#tm_mday=17, tm_hour=21, tm_min=26, tm_sec=3, tm_wday=2, tm_yday=198, tm_isdst=0)

#获取格式化时间
localtime = time.asctime(time.localtime(time.time()))
#print(localtime)
#Tue Feb 11 18:33:02 2016

#获取某月日历
import calendar
cal = calendar.month(2015,12)
#print(cal)
#显示2015年12月的日历

#strftime = time.strftime('%Y-%m-%d %H:%M:%S')
#print(strftime)

import datetime
dtime = datetime.datetime(year=2016,month=1,day=1)
print(dtime)
#2015-01-01 00:00:00
