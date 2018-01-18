import calendar
import json
from collections import deque
from datetime import datetime
from time import time

import pandas as pd
from pypika import Query, Table
from treq import get
from twisted.internet import defer
from twisted.internet import reactor, task

from server.api.utils import transform_tw_req
from server.db import get_dao

schema = [
    {
        'table_name': 'CURRENCY_PRICE_INFO',
        'pks'       : [
            {'request_time': 'integer'},
            {'cointype': 'text'}
        ],
        'fields'    : [
            {'transaction_date': 'text'},
            {'type': 'text'},
            {'units_traded': 'text'},
            {'price': 'integer'},
            {'a_cycle_price': 'integer'},
            {'b_cycle_price': 'integer'},
            {'c_cycle_price': 'integer'},
            {'d_cycle_price': 'integer'},
            {'e_cycle_price': 'integer'},
            {'f_cycle_price': 'integer'},
            {'g_cycle_price': 'integer'},
            {'total': 'text'}
        ]
    },
    {
        'table_name': 'KORBIT_RECENT_PRICE',
        'pks'       : [
            {'type': 'text'},
            {'time': 'integer'}
        ],
        'fields'    : [
            {'price': 'integer'}
        ]
    }
]

tk = None

recent_transaction_base_url = 'https://api.korbit.co.kr/v1/ticker'
currency_type_list = ['btc_krw', 'xrp_krw']
cycle_list = {}


def init_cycle_list_type():
    for coin_type in currency_type_list:
        cycle_list[coin_type] = [deque(maxlen=5), deque(maxlen=20), deque(maxlen=40), deque(maxlen=60),
                                 deque(maxlen=80), deque(maxlen=120), deque(maxlen=180)]


def convert(currency_type, data):
    ret = []

    ret.append(currency_type)
    ret.append(int(time()))

    price = int(data['last'])
    ret.append(price)
    return ret


def fetch_coin_finish(results, coin):
    for result, coin_type in zip(results, coin):
        info = convert(coin_type, json.loads(result[1]))
        VueService(get_dao()).insert_korbit_data(info)


def fetch_coin(url, params):
    def success_back(result):
        return result.content()

    def fail_back(fail):
        print(fail)
        return fail

    resp = get(url, params=params)
    resp.addCallbacks(success_back, fail_back)
    return resp


def get_currency_recent_transactions():
    dl = []

    for currency_type in currency_type_list:
        d = fetch_coin(recent_transaction_base_url, params={'currency_pair': currency_type})
        dl.append(d)

    dlist = defer.DeferredList(dl, consumeErrors=True)
    dlist.addCallback(fetch_coin_finish, currency_type_list)
    return dlist


def setup_currency_open_api():
    global tk
    tk = task.LoopingCall(get_currency_recent_transactions)
    tk.start(5)


def setup_service_env():
    init_cycle_list_type()
    reactor.callWhenRunning(setup_currency_open_api)


def stop_service_env():
    tk.stop()


class VueService:
    def __init__(self, db_handle):
        self._items = {}
        self.db_handle = db_handle

    @transform_tw_req
    @defer.inlineCallbacks
    def crypto_currerncies(self, request):
        message = yield defer.succeed('crypto_currerncies')
        print(request.args)
        datetime_objecta = datetime.strptime(
            '{}  {}'.format(request.args['startDate'][0], request.args['startTime'][0]),
            '%Y-%m-%d %I:%M%p')
        datetime_objectb = datetime.strptime(
            '{}  {}'.format(request.args['endDate'][0], request.args['endTime'][0]),
            '%Y-%m-%d %I:%M%p')

        data = self.avg(request.args['type'][0], calendar.timegm(datetime_objecta.utctimetuple()) - 32400,
                        calendar.timegm(datetime_objectb.utctimetuple()) - 32400)

        df = pd.DataFrame(data, columns=['time', 'b', 'c', 'd', 'e', 'price', '5', '20', '40', '60', '80', '120', '180',
                                         'total'])
        ma5 = df['price'].rolling(window=5).mean()
        df.insert(len(df.columns), 'ma5', ma5)

        ma20 = df['price'].rolling(window=20).mean()
        df.insert(len(df.columns), 'ma20', ma20)

        ma40 = df['price'].rolling(window=40).mean()
        df.insert(len(df.columns), 'ma40', ma40)

        ma60 = df['price'].rolling(window=60).mean()
        df.insert(len(df.columns), 'ma60', ma60)

        ma80 = df['price'].rolling(window=80).mean()
        df.insert(len(df.columns), 'ma80', ma80)

        ma120 = df['price'].rolling(window=120).mean()
        df.insert(len(df.columns), 'ma120', ma120)

        ma180 = df['price'].rolling(window=180).mean()
        df.insert(len(df.columns), 'ma180', ma180)

        defer.returnValue(df.to_json())

    def insert_korbit_data(self, currency_data):
        try:
            sql = '''INSERT INTO KORBIT_RECENT_PRICE( \
                                    type, \
                                    time, \
                                    price) \
                      VALUES(?,?,?)'''
            self.db_handle.run_operation(sql, currency_data)
        except Exception as e:
            print(e)
            raise

    def avg(self, cointype, start, end):
        table = Table('CURRENCY_PRICE_INFO')
        q = Query.from_(table).select(
            '*'
        ).where(
            (table.request_time >= start) & (table.request_time <= end) & (table.cointype == cointype)
        )
        rows = self.db_handle.run_fetch(str(q))
        return rows


def route(app):
    dao = get_dao()

    dao.create_table(schema)

    service = VueService(dao)
    app.route('/cryptoCurrencies')(service.crypto_currerncies)

    setup_service_env()
