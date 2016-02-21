#/usr/bin/python
#-*-coding:utf-8-*-

# 1
'''
 1. 类(Class)：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
 2. 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
 3. 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
 4. 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
 5. 实例变量：定义在方法中的变量，只作用于当前实例的类。
 6. 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
    例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
 7. 实例化：创建一个类的实例，类的具体对象。
 8. 方法：类中定义的函数。
 9. 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

'''

class Employee:
	'所有员工的基类'
	empCount  = 0

	'''
		第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
	'''
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		#类变量,类变量在整个实例化的对象中是公用的
		Employee.empCount += 1

	def displayCount(self):
		print('total empCount:',self.empCount)

	def displayInfo(self):
		print('empInfo:',self.name,self.salary)

emp1 = Employee('tom',2000)
emp2 = Employee('jack',3000)
emp3 = Employee('marry',4000)


print(Employee.empCount) # 3可以直接访问类变量
print(emp1.empCount)     # 3

emp1.displayCount() #3
emp1.displayInfo()  #tom 2000

emp2.displayCount() #3
emp2.displayInfo()  #jack 3000




# 2
'''
 getattr(obj, name[, default]) : 访问对象的属性。
 hasattr(obj,name) : 检查是否存在一个属性。
 setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
 delattr(obj, name) : 删除属性。
'''

emp1.age = 25
print(hasattr(emp1,'age')) #True
print(getattr(emp1,'gender','male')) #有则返回emp1.gender,无则设置emp1.gender = 'male'
print(setattr(emp1,'workYear',2)) #没有该属性，返回None，emp1.workYear = 2
print(emp1.workYear)  #2
del(emp1,workYear)
print(emp1.workYear)  #not define


# 3

#__doc__ :类的文档字符串
print(Employee.__doc__)  #所有员工的基类
#__name__: 类名
print(Employee.__name__) #Employee
#__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
print(Employee.__dict__) #
#__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
print(Employee.__module__) #__main__
#__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
print(Employee.__bases__) #(<class 'object'>,)



# 4. python对象销毁（垃圾回收）
'''
同Java语言一样，Python使用了引用计数这一简单技术来追踪内存中的对象。
在Python内部记录着所有使用中的对象各有多少引用。
一个内部跟踪变量，称为一个引用计数器。
当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。
但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。
'''
a = 40      # 创建对象  <40>
b = a       # 增加引用， <40> 的计数
c = [b]     # 增加引用.  <40> 的计数

del a       # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
c[0] = -1   # 减少引用 <40> 的计数

'''
垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。这种情况下，仅使用引用计数是不够的。
Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。
作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环
'''

class Point:
	def __init__(self,x = 0, y = 0):
		self.x =  x
		self.y = y

	'''
		析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
	'''
	def __del__(self):
		class_name = self.__class__.__name__
		print(class_name,'销毁')
		

pt1 = Point()
pt2 = pt1
pt3 = pt1

print( id(pt1), id(pt2), id(pt3)) #id相同


