import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define,options
define('port',default=8000,help='run on the given port',type=int)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
		    (r'/',MainHandler)
		]
		settings = dict(
				template_path = os.path.join(os.path.dirname(__file__),'templates'),
				static_path = os.path.join(os.path.dirname(__file__),'static'),
				debug = True
		)
		tornado.web.Application.__init__(self,handlers,**settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('indexbook.html',page_title = "'Burt's Book | Home",
        	header_text = "Welcome to Burt's Books!",
        	link="<a href='http://facebook'>facebookAddress</a>")	

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()        

