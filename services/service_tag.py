from flask import Flask, jsonify, Response
from flask_restx import Resource
from server import server
from bson.objectid import ObjectId
import unidecode
import datetime

app, api, mongo = server.app, server.api, server.mongo


def getOneTag(id):
    tagResult = mongo.db.tags.find_one({"_id":ObjectId(id)})
    if tagResult:
        tagResult['_id'] = str(tagResult['_id'])
        tagResult['id'] = tagResult.pop('_id')
        return jsonify(tagResult)
    else:
        return False


def getAllTags():
    tagResult = mongo.db.tags.find()
    cardList = []
    for c in tagResult:
        c['_id'] = str(c['_id'])
        c['id'] = c.pop('_id')
        cardList.append(c)
    if len(cardList) > 0:
        return jsonify(cardList)
    else:
        return False

def insertTag(body):
    body['data_criacao'] = datetime.datetime.now()
    nameConverter = body['name'].upper().split(' ')
    nameKeys = []
    for n in nameConverter:
        nameKeys.append(unidecode.unidecode(n))
    body['keys'] = nameKeys
    tagResult = mongo.db.tags.insert_one(body)
    if tagResult.inserted_id:
        return tagResult.inserted_id
    else:
        return False

def deleteTag(id):
    tagResult = mongo.db.tags.delete_one({"_id":ObjectId(id)})
    if tagResult.deleted_count == 1:
        return True
    else:
        return False

def updateTag(body,id):
    body['data_modificacao'] = datetime.datetime.now()
    tagResult = mongo.db.tags.update_one({"_id":ObjectId(id)}, {"$set": body})
    if tagResult.modified_count == 1:
        return True
    else:
        return False



