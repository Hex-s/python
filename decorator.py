#!/usr/bin/python
#-*-coding:utf-8-*-
import time

def log(func):
	def wrapper(*args,**kw):
		print('call: %s' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('now:%s' % time.time())




#now()
#print(now.__name__)  #wrapper

'''
如果decorator本身需要传入参数，
那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
'''
def log2(text):
	def decorate(func):
		def wrapper(*args,**kw):
			print('text:%s,call:%s' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorate

@log2('haha')
def nows():
	print('now:%s' % (time.time()))

#nows()
#print(nows.__name__) #wrapper

'''

不改变函数的__name__
functools
'''

import functools
def log3(func):
	@functools.wraps(func)
	def wraper(*args,**kw):
		print('logs')
	return wraper

@log3
def now3():
	print('now:%s' % (time.time()))

#now3()
#print(now3.__name__)


def log4(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
