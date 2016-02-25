#!/usr/bin/python
#-*-coding:utf-8-*-

'''
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:w3cschool.cc，这个是可选参数。
port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。

SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
from_addr: 邮件发送者地址。
to_addrs: 字符串列表，邮件发送地址。
msg: 发送消息

'''

import smtplib

def sendEmail():
	sender = 'from@fromdomain.com'
	receivers = ['to@todomain.com']

	message = """From: From Person <from@fromdomain.com>
		To: To Person <to@todomain.com>
		Subject: SMTP e-mail test

		This is a test e-mail message.
		"""

	try:
   		smtpObj = smtplib.SMTP('localhost')
   		smtpObj.sendmail(sender, receivers, message)         
   		print("Successfully sent email")
	except SMTPException:
   		print("Error: unable to send email")