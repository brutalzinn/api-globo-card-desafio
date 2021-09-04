from server import server
from controllers.controller_card import *
app, api = server.app, server.api

#ADVANCED LIST WITH PAGINATION FOR LIST ALL CARDS

api.add_resource(CardClass, '/v1/cards/list/<page>/<limit>', methods=["GET"])
api.add_resource(CardClass, '/v1/cards/<card_id>', methods=["GET","DELETE","PUT"])
api.add_resource(CardClass, '/v1/cards', methods=["POST","GET"])

