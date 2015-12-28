import tornado.ioloop
import tornado.web
import time

class SleepHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        time.sleep(10)
        self.write('awake')

class ImmediateHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('I am very fast')

application = tornado.web.Application([
        (r'/sleep', SleepHandler),
        (r'/immediate', ImmediateHandler)
    ])

if __name__ == '__main__':
    application.listen(9000)
    tornado.ioloop.IOLoop.current().start()
