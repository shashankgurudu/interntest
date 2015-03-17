import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pymongo

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [(r"/poem", WordHandler),(r'/', IndexHandler)]
		template_path=os.path.join(os.path.dirname(__file__), "templates")
		conn = pymongo.Connection("localhost", 27017)
		self.db = conn["example"]
		tornado.web.Application.__init__(self, handlers, debug=True)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class WordHandler(tornado.web.RequestHandler):
	def post(self):
		name = self.get_argument('name')
		email = self.get_argument('email')
		password = self.get_argument('password')
		phone = self.get_argument('phone')
		coll = self.application.db.words
		
		word_doc = {'name': name, 'email': email, 'password':password, 'phone':phone}
		coll.insert(word_doc)
		del word_doc["_id"]
		self.write(word_doc)

if __name__ == '__main__':
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())	
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
