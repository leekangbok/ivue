# from .coin import route as coin_route
from .qna import route as qna_route
from .rio import route as rio_route


def api_start(app):
    with app.subroute("/api") as app:
        # coin_route(app)
        qna_route(app)
        rio_route(app)
