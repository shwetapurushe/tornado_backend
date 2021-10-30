from tornado.httpserver import HTTPServer
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import tornado.options

from tornado.options import options, define

define("port", default=5600, help="run on the given port", type=int)


class MainHandler(RequestHandler):
    def get(self):
        self.write({'message': 'hello there Shweta!'})


def main():
    tornado.options.parse_command_line()
    # array of API routes, each route being a tuple (path, Handler)
    # array of API routes, each route being a tuple
    application = Application([(r"/", MainHandler)])
    # Serve the application
    http_server = HTTPServer(application)

    http_server.listen(options.port)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
