from flask import Flask, jsonify, Response
from flask_restx import Resource
from server import server
from bson.objectid import ObjectId
import datetime

app, api, mongo = server.app, server.api, server.mongo


def getOneCard(id):
    cardResult = mongo.db.cards.find_one({"_id":ObjectId(id)})
    if cardResult:
        cardResult['_id'] = str(cardResult['_id'])
        cardResult['id'] = cardResult.pop('_id')
        return jsonify(cardResult)
    else:
        return False


def getAllCards(tag_id):
    cardResult = mongo.db.cards.aggregate([{
   "$lookup":
     {
       "from": "tags",
       "localField": "tags",
       "foreignField": "_id",
       "as": "tags"
     }
}])
    cardList = []
    for c in cardResult:
        listTags = []
        c['_id'] = str(c['_id'])
        c['id'] = c.pop('_id')
        if 'tags' in c:
            for t in c['tags']:
                t['_id'] = str(t['_id'])
                t['id'] = t.pop('_id')
                listTags.append(t)
            c['tags'] = listTags
        cardList.append(c)
    if len(cardList) > 0:
        return jsonify(cardList)
    else:
        return False

def insertCard(body):
    body['data_criacao'] = datetime.datetime.now()
    listTags = []
    if 'tags' in body:
        for t in body['tags']:
            listTags.append(ObjectId(t))
        body['tags'] = listTags
    cardResult = mongo.db.cards.insert_one(body)
    if cardResult.inserted_id:
        return True
    else:
        return False

def deleteCard(id):
    cardResult = mongo.db.cards.delete_one({"_id":ObjectId(id)})
    if cardResult.deleted_count == 1:
        return True
    else:
        return False

def updateCard(body,id):
    body['data_modificacao'] = datetime.datetime.now()
    cardResult = mongo.db.cards.update_one({"_id":ObjectId(id)}, {"$set": body})
    if cardResult.modified_count == 1:
        return True
    else:
        return False



