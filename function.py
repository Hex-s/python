#!/usr/bin/python
#-*-coding:utf-8-*-

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

