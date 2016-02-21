class MethodText:
	name = 'method'
	__var = 'private'

	def func1(self):
		print('公有方法，func1',self.name,',',self.__var)
	
	def __func2(self):
		print('私有方法，func2',self.name,',',self.__var)

	'''
		类方法，调用属性和方法时才会被加载
	'''
	@classmethod
	def classFunc(self):
		print('类方法，classFunc',self.name,',',self.__var)

	'''
	静态方法，执行时，把所有的类，属性，方法加载完成，速度快，占用资源多
	'''
	@staticmethod
	def staticFunc():
		print('静态方法，staticFunc,',MethodText.__name__)

mt = MethodText()
mt.func1()
#mt.__func2()
mt.classFunc()
mt.staticFunc()

MethodText.classFunc()
MethodText.staticFunc()     #静态方法，staticFunc , MethodText
print(MethodText.__name__)  #MethodText

