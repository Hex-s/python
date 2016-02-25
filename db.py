#!/usr/bin/python
#-*-coding:utf-8-*-

# 导入MySQL驱动:
import mysql.connector

def dbWork():
	#设置连接信息
	conn = mysql.connector.connect(user='root', password='123', database='test')

	# 创建user表:
	cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')