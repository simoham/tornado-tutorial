import asyncio
import tornado
import cpuinfo, json, platform

from prometheus_client import start_http_server, Counter, Gauge, generate_latest
import time
import random

# Create Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
MEMORY_USAGE = Gauge('memory_usage_bytes', 'Current memory usage in bytes')

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


class MetricsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(generate_latest())


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hostname", HostnameHandler),
        (r"/api/v1.0/hello", ApiHelloHandler),
        (r"/metrics", MetricsHandler),
    ])

async def main():
    app = make_app()
    print("http://0.0.0.0:8888")
    app.listen(8888)
    await asyncio.Event().wait()

## Useless Test

if __name__ == "__main__":
    asyncio.run(main())
