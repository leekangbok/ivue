from itertools import chain


class MResult:
    success = 1
    message = ''
    count = 0


class MResponse:
    def __init__(self, item_cls):
        self.result = MResult()
        self.item_cls = item_cls
        self.items = []

    def add(self):
        item = self.item_cls()
        self.items.append(item)
        return item


class MRequest:
    def __init__(self, item, page=0, row_per_page=999999):
        self.item = item
        self.page = page
        self.row_per_page = row_per_page


class MItem:
    common_fields = ['uid', 'reg_date', 'mod_date']
    private_fields = []

    def __init__(self, **kwargs):
        for field in chain(self.common_fields, self.private_fields):
            setattr(self, field, None)

        for key in kwargs.keys():
            setattr(self, key, kwargs[key])
