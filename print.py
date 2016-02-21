#!/usr/bin/python
#-*-coding:utf-8-*-

'''
Python两种输出值的方式: 表达式语句 和 print() 函数。(第三种方式是使用文件对象的 write() 方法; 标准输出文件可以用 sys.stdout 引用。)

如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。

如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

str() 函数返回一个用户易读的表达形式。

repr() 产生一个解释器易读的表达形式。
'''

def rept_str():
	s = 'Hello'
	print(str(s))  #Hello
	print(repr(s)) #'Hello'

#rept_str()

def pow_three():
	for x in list(range(1,11)):
		print(repr(x).rjust(2),repr(x**2).rjust(3),end=' ')
		print(repr(x**3).rjust(4))
	print('********************')
	for x in list(range(1,11)):
		print('{0:2d} {1:3d} {2:4d}'.format(x,x**2,x**3))
	print('--------------------')
	print('12'.zfill(5))  #00012

pow_three()
'''
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
'''

'''
字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。同理，ljust() 和 center()
zfill(), 它会在数字的左边填充 0

'''

#替换
def fun(x,y):
	print('{}:{}'.format(x,y))

t = (1,2)
fun(*t)
#http://www.ziqiangxuetang.com/python3/python3-inputoutput.html
