import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("t1.html")

class HrefHandler(tornado.web.RequestHandler):
    def get(self,arg):
        a = arg
        self.write("href:"+a)

class HrefHandler2(tornado.web.RequestHandler):
    def get(self,arg1,arg2):
        self.write("href:: arg1:"+arg1+",arg2:"+arg2)        

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
          handlers=[
              (r"/", IndexHandler),
              (r"/a/(\w+)",HrefHandler),
              (r"/a/(\w+)/(\w+)",HrefHandler2),
          ],
          template_path = os.path.join(os.path.dirname(__file__),"ttemplates"),
          static_path = os.path.join(os.path.dirname(__file__),'sstatic'),
          debug = True,
          )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
