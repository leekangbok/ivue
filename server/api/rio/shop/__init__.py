from .service import route as service_route


def route(app):
    with app.subroute("/shop") as app:
        service_route(app)
