import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		if not self.get_secure_cookie('mycookie'):
			self.set_secure_cookie('mycookie','myvalue')
			self.write('Your cookie was not set yet!')
		else:
		    self.write('Your cookie was set!')

application = tornado.web.Application(
		[(r'/',MainHandler)],
		debug = True,
		cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
	)		    	

if __name__ == '__main__':
	application.listen(8000)
	tornado.ioloop.IOLoop.instance().start()