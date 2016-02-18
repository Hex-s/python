#!/usr/bin/python
#-*-coding:utf-8-*-

#@ def 函数
'''
# 1
def printMe(str):
	print(str)

printMe('asdasdasdssfa')
#-----------------------------------------------

#2
def printMe2(arg1,*kwargs):
	print(arg1)
	for k in kwargs:
		print(k)
printMe2(1,{2,3,4})
#-----------------------------------------------

#3
#lambda
g = lambda x:x**2
print(g(4))

a = list(range(1,6))
a1 = [i for i in a if i % 2 != 0]

def filterNum(x):
	return x%2 != 0
a2 = list(filter(filterNum,a))

a3 = list(filter(lambda x : x % 2 != 0,a))

print(a1,a2,a3)

#-------------
b = list(range(1,6))

b1 = [i + 1 for i in b ]
b2 = list(map(lambda x : x + 1 , b))

print(b1,b2)

#-------------
#python3中 reduce 在functools中
from functools import reduce

c = list(range(1,6))

c1 = reduce(lambda x,y : x + y , c)

print(c1)  #15
'''

#*****************************************************************

#@ 导入模块
'''
from modname import funcnane
from modname import *
import funcname

当你导入一个模块，Python解析器对模块位置的搜索顺序是：
	1.当前目录。
	2.如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
		windows：安装目录 c:\python3\lib                               
	3.如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

'''


#*****************************************************************

#@命名空间和作用域
MONEY = 100
def AddMoney():
	global MONEY
	MONEY += 100

print(MONEY)
AddMoney()
print(MONEY)