from tornado.httpserver import HTTPServer
from tornado.web import RequestHandler, Application, url
from tornado.ioloop import IOLoop
import tornado.options
from tornado.options import options, define

import api_v1

define("port", default=5600, help="run on the given port", type=int)


class MainHandler(RequestHandler):
    def get(self):
        self.write({'message': 'Welcome to my API!'})


class PingMessageHander(RequestHandler):
    def get(self):
        self.write({'message': 'Why, Hello there Shweta!'})


class TemplateHandler(RequestHandler):
    def get(self):
        self.render("index.html")


def main():
    tornado.options.parse_command_line()
    # array of API routes, each route being a tuple (path, Handler)

    api_routes = [
        url(r"/API/", MainHandler),
        url(r"/API/getPingMessage", PingMessageHander),
        url(r"/index.html", TemplateHandler)
        #url(r"/API/getLatestData", api_v1.getLatestData)
    ]

    application = Application(api_routes)
    # Serve the application
    http_server = HTTPServer(application)

    http_server.listen(options.port)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
