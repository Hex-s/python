import os.path
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
from tornado.options import define,options

define('port',default=8000,help='run on the given port',type=int)

class BookHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('book.html',title='book page',head='Books that are good',books=['python','tornado'])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
    	handlers=[(r'/',BookHandler)],
        template_path = os.path.join(os.path.dirname(__file__),'templates')
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()