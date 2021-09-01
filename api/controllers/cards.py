from flask import Flask, jsonify, Response
from flask_restx import Resource
from server import server


app, api, mongo = server.app, server.api, server.mongo

@api.route('/cards')
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
