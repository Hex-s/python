#-*-coding:utf-8-*-#
"""
	open/文件操作
	open(路径+文件名，读写模式，编码方式)
	读写模式：r只读，r+读写，w新建(会覆盖原有文件)，a追加，b二进制文件 如：‘rb,'wb','r+b'
	读写模式的类型有：
		rU 或 Ua 以读的方式打开，同时提供换行符支持
		w    以写的方式打开
		a    以追加模式打开(从EOF开始，必要时创建新文件)
		r+   以读写模式打开
		w+   以读写模式打开
		a+   以读写模式打开
		rb   以二进制读模式打开
		wb   以二进制写模式打开
		ab   以二进制追加模式打开
		rb+  以二进制读写模式打开
		wb+  以二进制读写模式打开
		ab+  以二进制读写模式打开

	PS:
		1.使用“W”，文件若存在，首先要清空，然后（重新）创建，
		2.使用“a”模式，把所有要写入文件的数据都追加到文件的末尾，即使使用了seek（）指向文件的其他地方，如果文件不存在，将自动被创建

	用法:
	1) f.read([size]) size未指定则返回整个文件,如果文件大小>2倍内存则有问题.f.read()读到文件尾时返回""(空字串)
	2) file.readline() 返回第一行
	3) file.readlines() 返回一个序列，每行是序列的一个元素
	4) file.readline([size])  返回包含size行的列表,size 未指定则返回全部行
	5) for line in file:print(line) #通过迭代器访问
	6) file.write('hello\n') 如果要写入字符串以外的数据,先将他转换为字符串
	7) file.tell() 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数)
	8) file.seek(偏移量,[起始位置])
		用来移动文件指针  偏移量:单位:比特,可正可负
		起始位置:0-文件头,默认值;1-当前位置;2-文件尾
	9) file.close()  关闭文件

	
"""

file = open('1.docx','a+')

#1
#content = file.read(5)

#2
#content = file.readline()

#3
#content = file.readlines()

#4
#content = file.readline(2)

#5
#for line in file:

#6
#file.write('hello\n')  #注意文件的打开方式

#7
#tell = file.tell()

#8
seek = file.seek(2)
print(seek)  #1

#print(content)

file.close()

