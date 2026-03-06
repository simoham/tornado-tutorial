import asyncio
import tornado
import cpuinfo, json, platform

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        message={"hostname": platform.node(), "cpu":cpuinfo.get_cpu_info()}
        self.write(json.dumps(message))


class HostnameHandler(tornado.web.RequestHandler):
    def get(self):
        message={"hostname": platform.node()}
        self.write(json.dumps(message))

class ApiHelloHandler(tornado.web.RequestHandler):
    def get(self):
        message={"hostname": platform.node()}
        self.write(json.dumps(message))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hostname", HostnameHandler),
        (r"/api/v1.0/hello", ApiHelloHandler),
    ])

async def main():
    app = make_app()
    print("http://0.0.0.0:8888")
    app.listen(8888)
    await asyncio.Event().wait()

## Useless Test

if __name__ == "__main__":
    asyncio.run(main())
