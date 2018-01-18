from .tech import route as tech_route


def route(app):
    with app.subroute("/ivue") as app:
        tech_route(app)
