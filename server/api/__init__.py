from server.api.doctor import route as doctor_route
from server.api.object import route as object_route
from server.api.policy import route as policy_route


def api_start(app):
    with app.subroute("/api") as app:
        policy_route(app)
        object_route(app)
        doctor_route(app)
