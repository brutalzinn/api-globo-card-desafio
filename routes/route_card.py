from server import server
from controllers.controller_card import *
app, api = server.app, server.api

#ADVANCED LIST WITH PAGINATION FOR LIST ALL CARDS
card_route = api.namespace('cards', description='Rotas de Cards')
card_route.add_resource(CardClass, '/list/<page>/<limit>', methods=["GET"])
card_route.add_resource(CardClass, '/<card_id>', methods=["GET","DELETE","PUT"])
card_route.add_resource(CardClass, '', methods=["POST","GET"])
