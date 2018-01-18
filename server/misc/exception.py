from contextlib import contextmanager


def exception_message(e):
    s, r = getattr(e, 'message', str(e)), getattr(e, 'message', repr(e))
    return s


@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


@contextmanager
def error_handle(resp):
    try:
        yield
    except Exception as e:
        resp.result.success = 0
        resp.result.message = exception_message(e)
    else:
        resp.result.success = 1
        resp.result.message = 'good'
