from server import server
from controllers.controller_card import *
app, api = server.app, server.api

api.add_resource(CardClass, '/v1/cards/list/<page>/<limit>')
api.add_resource(CardClass, '/v1/cards/<card_id>')
api.add_resource(CardClass, '/v1/cards')

