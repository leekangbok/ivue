from twisted.internet import defer

from server.api.utils import refine_twisted_web_request


class Service:
    def __init__(self):
        self._items = {}

    @refine_twisted_web_request
    @defer.inlineCallbacks
    def policy_forward_v4(self, request):
        message = yield defer.succeed('policy forward v4')
        defer.returnValue(message)


def route(app):
    service = Service()
    app.route('/v4')(service.policy_forward_v4)
