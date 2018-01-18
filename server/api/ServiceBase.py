from abc import ABC, abstractmethod
from functools import reduce
from operator import attrgetter
from time import time
from types import MappingProxyType

from pypika import Query
from twisted.internet import defer

from server.db import DaoIntegrityError
from server.misc.exception import error_handle
from server.misc.utils import generate_random_bits
from server.model.base import MItem


class ServiceBase(ABC):
    dao = None
    common_fields = list(MItem.common_fields)
    common_fields_getter = attrgetter(*common_fields)
    private_fields = []
    private_fields_getter = None
    table = None
    named_rec = None
    named_rec_prototype = None

    def __init__(self, dao):
        self.dao = dao

    @staticmethod
    def generate_uniq_uid():
        return generate_random_bits(64)

    def dict_to_named_rec(self, s):
        return self.named_rec_prototype._replace(**s)

    def row_to_named_rec(self, row, w_columns=None):
        if w_columns is None:
            return self.named_rec(*row)
        return self.dict_to_named_rec({k: v for k, v in zip(w_columns, row)})

    def set_item_attr(self, rec, item, transform=MappingProxyType({})):
        item.uid, item.reg_date, item.mod_date = self.common_fields_getter(rec)
        fields = self.private_fields
        for field in fields:
            f = transform.get(field)
            if f:
                f(item, getattr(rec, field))
            else:
                setattr(item, field, getattr(rec, field))

    def rec_to_item(self, rec, item):
        self.set_item_attr(rec, item)

    def set_where_statement(self, req, q):
        if req.item.uid:
            q = q.where(self.table.uid == req.item.uid)
        return q

    def set_sortby_statement(self, req, q):
        # if req.sortBy:
        #     q = q.orderby(req.sortBy,
        #                   order=enums.Order.desc if req.descending else enums.Order.asc)
        return q

    def set_offset_limit(self, req, q):
        # if req.row_per_page:
        #     q = q.limit(req.row_per_page)
        # if req.page:
        #     q = q.offset(req.page)
        return q

    @staticmethod
    @abstractmethod
    def create_response(**kwd):
        raise NotImplementedError

    def extract_column_values(self, item, transform=MappingProxyType({})):
        column_names = []
        column_values = []
        for n, v in zip(self.common_fields, self.common_fields_getter(item)):
            if v is not None:
                column_names.append(n)
                column_values.append(v)

        fields = self.private_fields
        if len(fields) > 1:
            for field in fields:
                f = transform.get(field)
                v = getattr(item, field, None)
                if v is not None:
                    column_names.append(field)
                    column_values.append(f(item, v) if f else v)
        else:
            f = transform.get(fields[0])
            v = getattr(item, fields[0], None)
            if v is not None:
                column_names.append(fields[0])
                column_values.append(f(item, v) if f else v)
        return column_names, column_values

    def create_update_statement(self, req, transform=MappingProxyType({})):
        req.item.mod_date = int(time())

        if req.item.uid:
            q = Query.update(self.table)
            column_names, column_values = self.extract_column_values(req.item, transform=transform)
            for name, value in ((name, value) for name, value in zip(column_names, column_values) if
                                name != 'uid'):
                q = q.set(name, value)
            q = q.where(self.table.uid == req.item.uid)
        else:
            req.item.uid = self.generate_uniq_uid()
            req.item.reg_date = int(time())
            q = Query.into(self.table)
            column_names, column_values = self.extract_column_values(req.item, transform=transform)
            q = q.columns(*column_names).insert(*column_values)
        return q

    @defer.inlineCallbacks
    def update_service(self, req, transform=MappingProxyType({}), **kwargs):
        resp = self.create_response(**kwargs)

        with error_handle(resp):
            in_loop, uid = 0, req.item.uid
            while True:
                try:
                    q = self.create_update_statement(req, transform)
                    yield self.dao.run_operation(str(q))
                except DaoIntegrityError:
                    req.item.uid = uid
                    in_loop += 1
                    if in_loop > 100:
                        raise
                except:
                    raise
                else:
                    break
        defer.returnValue(resp)

    def create_delete_statement(self, uids):
        q = Query.from_(self.table)
        if uids:
            q = q.where(self.table.uid.isin(uids)).delete()
        else:
            q = q.delete()
        return q

    @defer.inlineCallbacks
    def delete_service(self, req, **kwargs):
        resp = self.create_response(**kwargs)

        with error_handle(resp):
            q = self.create_delete_statement(req)
            yield self.dao.run_operation(str(q))

        defer.returnValue(resp)

    def create_search_statement(self, req, w_columns=None):
        if w_columns is not None:
            q = Query.from_(self.table).select(*w_columns)
        else:
            q = Query.from_(self.table).select('*')

        q = self.set_where_statement(req, q)
        q = self.set_sortby_statement(req, q)
        q = self.set_offset_limit(req, q)
        return q

    @defer.inlineCallbacks
    def search_service(self, req, w_columns=None, verify=lambda _: True, **kwargs):
        resp = self.create_response(**kwargs)

        start = req.page
        limit = req.row_per_page
        total = 0

        def fetch_all(it):
            nonlocal total
            for rec in (self.row_to_named_rec(i, w_columns) for i in it):
                if verify(rec):
                    if start <= total and resp.result.count < limit:
                        self.rec_to_item(rec, resp.add())
                        resp.result.count += 1
                    total += 1
            return resp

        with error_handle(resp):
            q = self.create_search_statement(req, w_columns)
            yield self.dao.run_fetch(str(q).replace('REGEX', 'REGEXP'), callback=fetch_all)
            resp.result.total = total

        defer.returnValue(resp)

    @staticmethod
    def set_like_statement(s, t, attr):
        if not t:
            return s
        if isinstance(t, (str, bytes)):
            t = [t]
        n = reduce(lambda x, y: x | y, (attr.like(''.join(['%', str(e), '%'])) for e in t))
        if s is not None:
            s |= n
        else:
            s = n

        return s

    @staticmethod
    def set_regexp_statement(s, t, attr):
        if not t:
            return s
        if isinstance(t, (str, bytes)):
            t = [t]
        n = attr.regex('|'.join(str(e) for e in t))
        if s is not None:
            s |= n
        else:
            s = n

        return s
