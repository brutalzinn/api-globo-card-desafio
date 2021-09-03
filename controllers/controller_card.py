from flask_restx import Resource
from server import server
from services.service_card import *

app, api, mongo = server.app, server.api, server.mongo

class CardClass(Resource):


    def get(self,card_id = None, tag_id = None, page = 1, limit = 3):
      if card_id == None:
        cards = getAllCards(tag_id, int(page) , int(limit))
        print('get all cards')
      else:
        cards = getOneCard(card_id)
      if cards is not False:
        return cards
      else:
        return ({"message":"Database is empty."}, 400)


    def post(self):
        req = api.payload
        if insertCard(req):
          return ({"message":"Card inserted successfully"}, 201)
        else:
          return ({"message":"Card cant be inserted"}, 400)


    def delete(self, card_id):
        if deleteCard(card_id):
          return ({"message":"Card deleted successfully"}, 200)
        else:
          return ({"message":"Card cant be deleted"}, 400)


    def put(self, card_id):
        req = api.payload
        if updateCard(req, card_id):
          return ({"message":"Card updated successfully"}, 200)
        else:
          return ({"message":"Card cant be updated"}, 400)


# api.add_resource(CardClass, '/cards/tag/<tag_id>')
api.add_resource(CardClass, '/cards/list/<page>/<limit>')
api.add_resource(CardClass, '/cards/<card_id>')
api.add_resource(CardClass, '/cards')