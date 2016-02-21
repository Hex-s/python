#!/usr/bin/python
#-*-coding:utf-8-*-

# 1 
'''
基类名写作括号里，基本类是在类定义的时候，在元组之中指明的。
在python中继承中的一些特点：
	1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
	2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
	3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
'''
'''
class Parent:
	parentAttr = 100
	def __init__(self):
		print('调用父类的构造方法')

	def parentMethod(self):
		print('调用父类方法')
		#return 0

	def setAttr(self,attr):
		Parent.parentAttr = attr

	def getAttr(self):
		print('父类属性：',Parent.parentAttr)

class Child(Parent):
	def __init__(self):
		print('调用子类的构造方法')

	def childMethod(self):
		print('调用子类方法')


c = Child()     #调用子类的构造方法
c.childMethod() #用子类方法
print(c.parentAttr)  #100
print(c.parentMethod())  #调用父类方法，方法没有return，会返回None
c.setAttr(200)
print(c.getAttr())
'''

# 2
'''
issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
'''

'''
c = Child() 
print(isinstance(c,Child))   #True
print(issubclass(Child,Parent)) #True
'''

# 3 方法重写
'''
方法重写
	如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
'''
'''
class Parent2:
	def myMethod(self):
		print('父类方法')

class Child2:
	def myMethod(self):
		print('子类方法')

c2 = Child2()
c2.myMethod()
'''

#3 
class c1:
	name = 'c1'

class c2:
	name = 'c2'
class c3(c1,c2):
	pass

c = c1()
#print(c.name)  #c1

class cc1:
	name = 'cc1'
	def __init__(self):
		self.name = 'cc_1'
		print('cc1.__init__')

class cc2:
	name = 'cc2'
	def __init__(self):
		self.name = 'cc_2'
		print('cc2.__init__')

class cc3(cc1,cc2):
	name = 'cc3'
	def __init__(self):
		print('cc3.__init__')
		cc2.__init__(self)


cc = cc3()
'''
if cc3没有构造方法:执行了cc1的构造方法  cc.name = cc_1
elif cc3.__init__调用了其他父类的__init__则使用调用父类的方法 cc.name = 'cc_2'
else cc3有自己的__init cc.name = 'cc_3'
'''
print(cc.name) #cc_1 

