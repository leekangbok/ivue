from .ivue import route as ivue_route


def route(app):
    with app.subroute("/qna") as app:
        ivue_route(app)
