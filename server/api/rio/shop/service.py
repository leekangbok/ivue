import json

from twisted.internet import defer

from server.api.utils import transform_tw_req
from .edent import get_prices as get_edent_prices
from .kdental import get_prices as get_kdental_prices


class Service:
    @transform_tw_req
    @defer.inlineCallbacks
    def shop_get_all(self, request):
        dl = list()

        dl.append(get_edent_prices(request))
        dl.append(get_kdental_prices(request))

        dlist = defer.DeferredList(dl, consumeErrors=True)

        content = yield dlist
        print(content)
        defer.returnValue(json.dumps(content))


def route(app):
    service = Service()
    app.route('/items', methods=['GET'])(service.shop_get_all)
