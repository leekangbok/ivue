from .crypto_currency.service import route as crypto_currency_route


def route(app):
    with app.subroute("/coin") as app:
        crypto_currency_route(app)
