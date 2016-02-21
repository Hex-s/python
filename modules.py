#!/usr/bin/python
#-*-coding:utf-8-*-

'''
package 中要有__init__.py文件，才能进行import
'''
from class_basic import Employee as emp

class emp_print:
	e = emp('tom',10000)
	print(emp.empCount)

'''
直接调用时会执行，被当成模块时不执行
'''
if __name__ == '__main__':
	e_p = emp_print()
else:
	print('imported')