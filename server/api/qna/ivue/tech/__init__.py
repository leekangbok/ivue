from .service import route as service_route


def route(app):
    with app.subroute("/tech") as app:
        service_route(app)
