import asyncio
import tornado
import cpuinfo, json, platform

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        message={"hostname": platform.node(), "cpu":cpuinfo.get_cpu_info()}
        self.write(json.dumps(message))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    print("http://0.0.0.0:8888")
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
