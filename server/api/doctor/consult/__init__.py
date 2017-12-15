from twisted.internet import defer

from server.api.utils import refine_twisted_web_request


class Service:
    @refine_twisted_web_request
    @defer.inlineCallbacks
    def consults(self, request):
        message = yield defer.succeed('consult get')
        defer.returnValue(message)


def route(app):
    service = Service()
    app.route('/consult', methods=['GET'])(service.consults)
