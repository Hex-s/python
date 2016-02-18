'''
如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
'''
def expError():
	try:
		score = int('1234')
	except:
		print("it's not a number")
	else:
		print('ok')

#expError()

'''
try-finally 语句无论是否发生异常都将执行最后的代码。中间不能加except
'''
def IOError1():
	try:
   		fh = open("testfile", "w")
   		fh.write("This is my test file for exception handling!!")
	finally:
		print('last')
		fh.close()
   		

#IOError1()

def IOError2():
	try:
		fh = open("testfile", "w")
		try:
			fh.write("This is my test file for exception handling!!")
		finally:
			print("Going to close the file")
			fh.close()
	except IOError:
		print("Error: can\'t find file or read data")

#IOError2()


'''
一个异常可以带上参数，可作为输出的异常信息参数。

'''
def temp_convert(var):
	try:
		return int(var)
	except ValueError, Argument:
		print "The argument does not contain numbers\t", Argument 

ErrorArgument('a')