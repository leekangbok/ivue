import collections
import json
from operator import attrgetter

import jsonpickle
from pypika import Table
from twisted.internet import defer

from server.api.ServiceBase import ServiceBase
from server.api.utils import transform_tw_req
from server.db import get_dao
from server.model.base import MResponse, MRequest, MItem

table = Table('qna_vue_tech')


class Item(MItem):
    private_fields = ['subject', 'body', 'author', 'view_count', 'tag_count', 'key', 'parent']


class Service(ServiceBase):
    def __init__(self, dao):
        super().__init__(dao)
        self.table = table

    @staticmethod
    def create_response(**kwargs):
        return MResponse(Item)

    @transform_tw_req
    @defer.inlineCallbacks
    def tech_get_all(self, request):
        req = MRequest(Item(author=request.args.get('author', [None])[0],
                            subject=request.args.get('subject', [None])[0],
                            body=request.args.get('body', [None])[0],
                            reg_date=request.args.get('reg_date', [None])[0]),
                       request.args.get('page', [0])[0],
                       request.args.get('row_per_page', [9999999])[0])
        resp = yield self.search_service(req, w_columns=request.args.get('w_columns', None))
        defer.returnValue(jsonpickle.encode(resp, unpicklable=False))

    @transform_tw_req
    @defer.inlineCallbacks
    def tech_get(self, request, uid):
        req = MRequest(Item(uid=uid))
        resp = yield self.search_service(req)
        defer.returnValue(jsonpickle.encode(resp, unpicklable=False))

    @transform_tw_req
    @defer.inlineCallbacks
    def tech_create(self, request):
        content = json.loads(request.content.read())
        req = MRequest(Item(**content))
        resp = yield self.update_service(req)
        defer.returnValue(jsonpickle.encode(resp, unpicklable=False))

    @transform_tw_req
    @defer.inlineCallbacks
    def tech_update(self, request, uid):
        content = json.loads(request.content.read())
        req = MRequest(Item(**content, uid=uid))
        resp = yield self.update_service(req)
        defer.returnValue(jsonpickle.encode(resp, unpicklable=False))

    @transform_tw_req
    @defer.inlineCallbacks
    def tech_delete(self, request, uid):
        resp = yield self.delete_service([uid])
        defer.returnValue(jsonpickle.encode(resp, unpicklable=False))

    def set_where_statement(self, req, q):
        q = super().set_where_statement(req, q)
        if req.item.author:
            author = self.set_like_statement(None, req.item.author, self.table.author)
            q = q.where(author)
        if req.item.subject:
            subject = self.set_like_statement(None, req.item.subject, self.table.subject)
            q = q.where(subject)
        if req.item.body:
            body = self.set_like_statement(None, req.item.body, self.table.body)
            q = q.where(body)
        if req.item.reg_date:
            # 2018.9.11-2018.12.31
            pass
        return q


def route(app):
    get_dao().create_table('create table if not exists {} '
                           '('
                           '{} text, {} integer default 0, {} integer default 0, '
                           '{} text default "", '
                           '{} text default "", '
                           '{} text default "", '
                           '{} integer default 0, '
                           '{} integer default 0, '
                           '{} text default "", '
                           '{} text default "", '
                           'primary key (uid)'
                           ')'.format(table.table_name, *MItem.common_fields, *Item.private_fields))

    Service.private_fields = list(Item.private_fields)
    Service.private_fields_getter = attrgetter(*Service.private_fields)
    Service.named_rec = collections.namedtuple(table.table_name, ' '.join(
        [*Service.common_fields, *Service.private_fields]))
    Service.named_rec_prototype = Service.named_rec('', 0, 0, '', '', '', 0, 0, '', '')

    service = Service(get_dao())

    app.route('/items', methods=['GET'])(service.tech_get_all)
    app.route('/items/<string:uid>', methods=['GET'])(service.tech_get)
    app.route('/items', methods=['POST'])(service.tech_create)
    app.route('/items/<string:uid>', methods=['PUT'])(service.tech_update)
    app.route('/items/<string:uid>', methods=['DELETE'])(service.tech_delete)
