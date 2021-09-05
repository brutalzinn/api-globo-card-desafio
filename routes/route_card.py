from server import server
from controllers.controller_card import *
app, api = server.app, server.api


card_route = api.namespace('cards', description='Rotas de Cards')
card_route.add_resource(card_class_extra, '/list/<page>/<limit>', methods=["GET"])
card_route.add_resource(card_class, '/<card_id>', methods=["GET","DELETE","PUT"])
card_route.add_resource(card_class, '', methods=["POST"])
