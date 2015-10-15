import web

web.config.debug = False

urls = ("/.*", "hello")
app = web.application(urls, globals())


class hello:
    def GET(self):
        return 'Hello, world!'

application = wsgiapp = app.wsgifunc()

if __name__ == "__main__":
    app.run()
