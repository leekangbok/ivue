from .shop import route as shop_route


def route(app):
    with app.subroute("/rio") as app:
        shop_route(app)
