from flask import Flask, jsonify, Response
from flask_restx import Resource
from server import server
from bson.objectid import ObjectId
import datetime
import math
from utils.utils_tag import *

app, api, mongo = server.app, server.api, server.mongo


def getOneCard(id):

    filters = [{
    "$lookup":
     {
       "from": "tags",
       "localField": "tags",
       "foreignField": "_id",
       "as": "tags"
     }
    },
    {"$match": {"_id": ObjectId(id)}}
    ]
    cardResult = mongo.db.cards.aggregate(filters)
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


def getAllCards(tag_id, page , limit):
    filters = [{
   "$lookup":
     {
       "from": "tags",
       "localField": "tags",
       "foreignField": "_id",
       "as": "tags"
     }
},
{ "$sort": { "data_criacao": -1}},
{ "$skip": (page - 1)* limit},
{ "$limit": limit * 1 }]


    if tag_id:
        filters.append({"$match": {
        "tags._id": ObjectId(tag_id)
      }})
    cardResult = mongo.db.cards.aggregate(filters)

    calcPages = mongo.db.cards.find().count() % limit
    totalPage = 0
    if calcPages != 0:
        totalPage = totalPage + 1
    totalPage = totalPage + math.trunc(mongo.db.cards.find().count() / limit)

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
        return {"totalPage":totalPage,"currentPage":page,"total":len(cardList),"cards":cardList}
    else:
        return False

def insertCard(body):
    body['data_criacao'] = datetime.datetime.now()
    if 'tags' in body:
        body['tags'] = tagCreator(body['tags'])
    cardResult = mongo.db.cards.insert_one(body)
    if cardResult.inserted_id:
        return True
    else:
        return False

def deleteCard(id):
    cardFinder = mongo.db.cards.find_one({"_id":ObjectId(id)})
    if "tags" in cardFinder:
        tagDelete(cardFinder['tags'])


    cardResult = mongo.db.cards.delete_one({"_id":ObjectId(id)})
    if cardResult.deleted_count == 1:
        return True
    else:
        return False

def updateCard(body,id):
    body['data_modificacao'] = datetime.datetime.now()
    cardFinder = mongo.db.cards.find_one({"_id":ObjectId(id)})
    if 'tags' in body:
        tagDelete(cardFinder['tags'])
        body['tags'] = tagCreator(body['tags'])
    cardResult = mongo.db.cards.update_one({"_id":ObjectId(id)}, {"$set": body})
    if cardResult.modified_count == 1:
        return True
    else:
        return False



