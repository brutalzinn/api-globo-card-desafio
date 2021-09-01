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
          cardList.append({'id':str(c['_id']),'texto': c['texto'],'tags':c['tags']})
        return jsonify(cardList)

    def post(self):
        req_data = api.payload
        mongo.db.cards.insert_one(req_data)
        return ({"message":"Card inserted successfully"}, 200)
    def delete(self,card_id):
        mongo.db.cards.delete_one({"_id":ObjectId(card_id)})
        print('trying to delete',card_id)
        return ({"message":"Card deleted successfully"}, 200)


api.add_resource(CardClass, '/cards/<card_id>')
api.add_resource(CardClass, '/cards/')