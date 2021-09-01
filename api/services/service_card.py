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
        return jsonify(cardResult)
    else:
        return False


def getAllCards():
    cardResult = mongo.db.cards.find()
    cardList = []
    for c in cardResult:
        if 'tags' in c:
            cardList.append({'_id':str(c['_id']),'texto': c['texto'],'tags':c['tags']})
        else:
            cardList.append({'_id':str(c['_id']),'texto': c['texto']})
    if len(cardList) > 0:
        return jsonify(cardList)
    else:
        return False

def insertCard(body):
    body['data_criacao'] = datetime.datetime.now()
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



