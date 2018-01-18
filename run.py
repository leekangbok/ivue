import os

from klein import Klein
from twisted.internet import _sslverify, reactor
from twisted.web.static import File

from server.api import api_start
from server.db import set_dao
from server.db.sqlite import DBSQLite3

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


def serve():
    def shutdown():
        ShutDown.stop = True

    reactor.addSystemEventTrigger('before', 'shutdown', shutdown)

    set_dao(DBSQLite3())

    api_start(app)

    port = int(os.environ.get('PORT', 5000))

    app.run("0.0.0.0", port)


if __name__ == '__main__':
    serve()
