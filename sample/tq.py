import json
import pprint

from treq import get
from twisted.internet import task, defer


def fetch_coin_finish(results, coin):
    for result, coin_type in zip(results, coin):
        pprint.pprint(json.loads(result[1]))
        print(coin_type)


def fetch_coin(url):
    def success_back(result):
        return result.content()

    def fail_back(fail):
        return fail

    resp = get(url)
    resp.addCallbacks(success_back, fail_back)
    return resp


def action():
    # coin_type = ['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP', 'BCH', 'XMR', 'ZEC', 'QTUM', 'BTG', 'EOS']
    coin_type = ['BTC']
    base_url = 'https://api.bithumb.com/public/recent_transactions/{}'
    dl = []

    for t in coin_type:
        d = fetch_coin(base_url.format(t))
        dl.append(d)

    dlist = defer.DeferredList(dl, consumeErrors=True)
    dlist.addCallback(fetch_coin_finish, coin_type)
    return dlist


def looping():
    tk = task.LoopingCall(action)
    tk.start(5)
