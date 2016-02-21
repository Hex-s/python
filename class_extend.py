#/usr/bin/python
#-*-coding:utf-8-*-

# 1 
'''
基类名写作括号里，基本类是在类定义的时候，在元组之中指明的。
在python中继承中的一些特点：
	1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
	2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
	3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
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


# 2
'''
issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
'''

c = Child() 
print(isinstance(c,Child))   #True
print(issubclass(Child,Parent)) #True

# 3 方法重写
'''
方法重写
	如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
'''

class Parent2:
	def myMethod(self):
		print('父类方法')

class Child2:
	def myMethod(self):
		print('子类方法')

c2 = Child2()
c2.myMethod()


# 4 基础重载方法
'''
基础重载方法
1	__init__ ( self [,args...] )
		构造函数
		简单的调用方法: obj = className(args)
2	__del__( self )
		析构方法, 删除一个对象
		简单的调用方法 : dell obj
3	__repr__( self )
		转化为供解释器读取的形式
		简单的调用方法 : repr(obj)
4	__str__( self )
		用于将值转化为适于人阅读的形式
		简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
		对象比较
		简单的调用方法 : cmp(obj, x)

'''

class Vector:
	'Python同样支持运算符重载'
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def __str__(self):
		return '(%d,%d)' % (self.a,self.b)

	def __add__(self,other):
		return Vector(self.a+other.a,self.b+other.b)

v1 = Vector(1,2)
v2 = Vector(3,4)
print(v1+v2)  #(4,6),如果没有__str__,返回的是一个Vector对象，有了，则会将返回到对象在进行__str__后返回


# 5 类属性与方法
'''
类的私有属性
	__privateAttrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__privateAttrs。
类的方法
	在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
类的私有方法
	__privateMethod：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__privateMethods
'''

class JustCounter:
	__sectetCount = 0 #私有变量
	publicCount = 0 #公开变量

	def count(self):
		self.__sectetCount += 1
		self.publicCount += 1
		self.__add()

	def __add(self):
		self.__sectetCount += 2
		print('__sectetCount:',self.__sectetCount,',publicCount:',self.publicCount)

count = JustCounter()
print(count.publicCount) #0
count.count()  #__sectetCount: 3 ,publicCount: 1
print(count.publicCount) #1
#print(count.__sectetCount)  #no attribute
'''
Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
'''
print(count._JustCounter__sectetCount) #3
print(count.__add())  #no attribute



