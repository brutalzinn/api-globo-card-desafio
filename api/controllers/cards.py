from flask import Flask, jsonify, Response
from flask_restx import Resource
from server import server
from bson.objectid import ObjectId


app, api, mongo = server.app, server.api, server.mongo

class CardClass(Resource):
    def get(self):
        cards = mongo.db.cards.find()
        cardList = []
        for c in cards:
          if 'tags' in c:
            cardList.append({'id':str(c['_id']),'texto': c['texto'],'tags':c['tags']})
          else:
            cardList.append({'id':str(c['_id']),'texto': c['texto']})
        return jsonify(cardList)

    def post(self):
        req = api.payload
        mongo.db.cards.insert_one(req)
        return ({"message":"Card inserted successfully"}, 200)
    def delete(self,card_id):
        mongo.db.cards.delete_one({"_id":ObjectId(card_id)})
        print('trying to delete',card_id)
        return ({"message":"Card deleted successfully"}, 200)
    def put(self, card_id):
        req = api.payload
        mongo.db.cards.update_one({"_id":ObjectId(card_id)}, {"$set": req})
        return ({"message":"Card updated successfully"}, 200)



api.add_resource(CardClass, '/cards/<card_id>')
api.add_resource(CardClass, '/cards')