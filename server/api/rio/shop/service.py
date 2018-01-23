import json

from twisted.internet import defer

from server.api.utils import transform_tw_req
from server.misc.utils import flatten
from .edent import get_products as get_edent_products


class Service:
    @transform_tw_req
    @defer.inlineCallbacks
    def shop_get_all(self, request):
        product = request.args.get('product', [''])[0]
        if not product:
            defer.returnValue(json.dumps([]))

        dl = list()

        dl.append(get_edent_products(product))
        # dl.append(get_kdental_prices(request, product))

        dlist = defer.DeferredList(dl, consumeErrors=True)

        content = yield dlist
        content = list(flatten((e[1] for e in content if e[0]), ignore_types=(str, bytes, dict)))
        defer.returnValue(json.dumps(content))


def route(app):
    service = Service()
    app.route('/items', methods=['GET'])(service.shop_get_all)
