from decorator import decorator
from twisted.web.server import Request


def _byte_to_str(data):
    if isinstance(data, bytes):
        return data.decode()
    if isinstance(data, (str, int)):
        return str(data)
    if isinstance(data, dict):
        return dict(map(_byte_to_str, data.items()))
    if isinstance(data, tuple):
        return tuple(map(_byte_to_str, data))
    if isinstance(data, list):
        return list(map(_byte_to_str, data))
    if isinstance(data, set):
        return set(map(_byte_to_str, data))


@decorator
def transform_tw_req(func, *args, **kwargs):
    if isinstance(args[0], Request):
        args[0].args = _byte_to_str(args[0].args)
    else:
        args[1].args = _byte_to_str(args[1].args)
    return func(*args, **kwargs)
