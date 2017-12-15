import os

from klein import Klein
from twisted.internet import _sslverify, reactor
from twisted.web.static import File

_sslverify.platformTrust = lambda: None

app = Klein()


@app.route('/static/', branch=True)
def static(_):
    return File('./dist/static')


@app.route("/")
def index(_):
    return File('./dist/index.html')


@app.route("/index.html")
def index(_):
    return File('./dist/index.html')


class ShutDown:
    stop = False


class ShuttingDown(Exception):
    pass


def serve():
    def shutdown():
        ShutDown.stop = True

    reactor.addSystemEventTrigger('before', 'shutdown', shutdown)

    port = int(os.environ.get('PORT', 5000))

    app.run("0.0.0.0", port)


if __name__ == '__main__':
    serve()
