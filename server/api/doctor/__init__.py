from .consult import route as consult_route
from .member import route as member_route


def route(app):
    with app.subroute("/doctor") as app:
        consult_route(app)
        member_route(app)
