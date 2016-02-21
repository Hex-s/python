#!/usr/bin/python
#-*-coding:utf-8-*-

#@ def 函数

# 1
def printMe(str):
	print(str)

printMe('asdasdasdssfa')
#-----------------------------------------------

#2 传参
def printMe2(arg1,*kwargs):
	print(arg1)
	for k in kwargs:
		print(k)
printMe2(1,{2,3,4})

def fun(name='haha',age=20):
	print(name,',',age)

# 1)
fun()  			#haha,20
# 2)
fun('tom')      #tom,20
# 3)
fun(20)         #20,20
# 4)
fun(age=25)		#haha,25
# 5)
t = ('jack',50)
fun(*t)         #jack,50
# 6)
dict = {'name':'tom','age':30}
fun(**dict)     #tom,30
#-----------------------------------------------

#3 lambda
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

# 1.声明法
MONEY = 100
def AddMoney():
	global MONEY
	MONEY += 100

print(MONEY)
AddMoney()
print(MONEY)

# 2.模块法（推荐）
#gl.py
gl_1 = 'hello'
gl_2 = 'world'

#a.py
import gl

def hello_print():
	print(gl.gl_1,gl.gl_2)

#b.py
'''
第二种方法，适用于不同文件之间的变量共享,避免如下问题：可能会导致全局变量的不可预知性；全局变量降低了代码的可读性
'''
import gl

def func1():
	gl.gl_1 = 'HELLO'
	gl.gl_2 = 'WORLD'

#*****************************************************************

'''
globals() 和 locals() 函数

根据调用地方的不同，globals()和locals()函数可被用来返回全局和局部命名空间里的名字。
如果在函数内部调用locals()，返回的是所有能在该函数里访问的命名。
如果在函数内部调用globals()，返回的是所有在该函数里能访问的全局名字。
两个函数的返回类型都是字典。所以名字们能用keys()函数摘取。

reload()函数

当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
因此，如果你想重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块。语法如下：
reload(hello)
'''




