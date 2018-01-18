g_dao = None


class DaoIntegrityError(Exception):
    pass


class DBBase:
    def get_all_column_name(self, tablename):
        pass

    def get_column_name(self, tablename):
        pass

    def create_table(self, statement):
        pass

    def run_operation(self, statement, *args):
        pass

    def run_fetch(self, query, callback):
        pass


def set_dao(dao):
    global g_dao

    assert g_dao is None
    assert isinstance(dao, DBBase)
    g_dao = dao


def get_dao():
    assert g_dao is not None
    return g_dao
