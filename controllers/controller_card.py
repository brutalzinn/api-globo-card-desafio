from flask.helpers import make_response
from flask_restx import Resource
from server import server
from services.service_card import *
from models.models_card import Card
from flask_restx import fields


app, api = server.app, server.api

# @api.tags = [{
#             "name": "Cards",
#             "description": "Rotas de cards"
#         }]

card_body_field = api.model('Cards', {
    'texto': fields.String(description='Texto do card', required=True, enum=["texto"]),
    'tags': fields.List(fields.String(enum=["tag1"]),description='Array com nome de tags')
})
class card_class_extra(Resource):
  @api.doc(params={'limit': 'Máximo de itens por página','page':'Número da página'})
  def get(self, page:int, limit:int):
      cards = getAllCards(int(page), int(limit))
      if cards is not False:
        return make_response(cards,200)
      else:
        return ({"message":"Database is empty."}, 400)
class card_class(Resource):
    @api.doc(params={'card_id': 'Identificador único'})
    def get(self, card_id):

      cards = getOneCard(card_id)
      if cards is not False:
        return make_response(cards,200)
      else:
        return ({"message":"Database is empty."}, 400)

    @api.doc(body=card_body_field)
    def post(self):
        req = api.payload
        card = Card(req)
        if not card.validate():
          return ({"message":"Invalid input"}, 400)
        if insertCard(req):
          return make_response({"message":"Card inserted successfully"},201)
        else:
          return ({"message":"Card cant be inserted"}, 400)

    @api.doc(params={'card_id': 'Identificador único'})
    def delete(self, card_id):
        if deleteCard(card_id):
          return ({"message":"Card deleted successfully"}, 200)
        else:
          return ({"message":"Card cant be deleted"}, 400)

    @api.doc(body=card_body_field,params={'card_id': 'Identificador único'})
    def put(self, card_id):
        req = api.payload
        card = Card(req)
        if not card.validate():
          return ({"message":"Invalid input"}, 400)
        if updateCard(req, card_id):
          return ({"message":"Card updated successfully"}, 200)
        else:
          return ({"message":"Card cant be updated"}, 400)
