#!/usr/bin/python
#-*-coding:utf-8-*-

'''
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，
派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
'''
class Text():
	def p(self):
		print('hello')

Text().p()