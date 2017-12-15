import json

from twisted.internet import defer

from server.api.utils import refine_twisted_web_request

sample = [
    {
        'value'   : False,
        'name'    : 'Frozen Yogurt',
        'calories': 159,
        'fat'     : 6.0,
        'carbs'   : 24,
        'protein' : 4.0,
        'sodium'  : 87,
        'calcium' : '14%',
        'iron'    : '1%'
    },
    {
        'value'   : False,
        'name'    : 'Ice cream sandwich',
        'calories': 237,
        'fat'     : 9.0,
        'carbs'   : 37,
        'protein' : 4.3,
        'sodium'  : 129,
        'calcium' : '8%',
        'iron'    : '1%'
    },
    {
        'value'   : False,
        'name'    : 'Eclair',
        'calories': 262,
        'fat'     : 16.0,
        'carbs'   : 23,
        'protein' : 6.0,
        'sodium'  : 337,
        'calcium' : '6%',
        'iron'    : '7%'
    },
    {
        'value'   : False,
        'name'    : 'Cupcake',
        'calories': 305,
        'fat'     : 3.7,
        'carbs'   : 67,
        'protein' : 4.3,
        'sodium'  : 413,
        'calcium' : '3%',
        'iron'    : '8%'
    },
    {
        'value'   : False,
        'name'    : 'Gingerbread',
        'calories': 356,
        'fat'     : 16.0,
        'carbs'   : 49,
        'protein' : 3.9,
        'sodium'  : 327,
        'calcium' : '7%',
        'iron'    : '16%'
    },
    {
        'value'   : False,
        'name'    : 'Jelly bean',
        'calories': 375,
        'fat'     : 0.0,
        'carbs'   : 94,
        'protein' : 0.0,
        'sodium'  : 50,
        'calcium' : '0%',
        'iron'    : '0%'
    },
    {
        'value'   : False,
        'name'    : 'Lollipop',
        'calories': 392,
        'fat'     : 0.2,
        'carbs'   : 98,
        'protein' : 0,
        'sodium'  : 38,
        'calcium' : '0%',
        'iron'    : '2%'
    },
    {
        'value'   : False,
        'name'    : 'Honeycomb',
        'calories': 408,
        'fat'     : 3.2,
        'carbs'   : 87,
        'protein' : 6.5,
        'sodium'  : 562,
        'calcium' : '0%',
        'iron'    : '45%'
    },
    {
        'value'   : False,
        'name'    : 'Donut',
        'calories': 452,
        'fat'     : 25.0,
        'carbs'   : 51,
        'protein' : 4.9,
        'sodium'  : 326,
        'calcium' : '2%',
        'iron'    : '22%'
    },
    {
        'value'   : False,
        'name'    : 'KitKat',
        'calories': 518,
        'fat'     : 26.0,
        'carbs'   : 65,
        'protein' : 7,
        'sodium'  : 54,
        'calcium' : '12%',
        'iron'    : '6%'
    }
]


class Service:
    @refine_twisted_web_request
    @defer.inlineCallbacks
    def members(self, request):
        request.setHeader('Content-Type', 'application/json')
        message = yield defer.succeed(json.dumps(dict(items=sample)))
        defer.returnValue(message)


def route(app):
    service = Service()
    app.route('/member', methods=['GET'])(service.members)
