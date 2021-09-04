from bson.objectid import ObjectId
from flask.json import jsonify
from flask_restx import Resource
from flask import Response
from server import server
import math
app, api, mongo = server.app, server.api, server.mongo

#ADVANCED SEARCH ROUTE WITH PAGINATION
@app.route('/v1/search/<page>/<limit>', methods=["POST"])
def search(page, limit):
    page = int(page)
    limit = int(limit)
    print('Search hello world',api.payload['key'])
    keys = api.payload['key'].upper().split(" ")

    regex = ''
    for k in keys:
        regex = f'^{k}|' + regex

    max = len(regex)
    n = 1
    regexFinal = ''

    for l in regex:
        print(l)
        if n != max:
            regexFinal = regexFinal + l
            n = n + 1
        else:
            break

    filters = { "keys": { "$regex": regexFinal, "$options": "i" }}
    # print(regexFinal)
    # tagsResult = mongo.db.tags.find_one(filters)
    # if tagsResult is None:
    #     return ({"message":f"Cant find by {api.payload['key']}"}, 400)
    filtersAdvanced = [{
   "$lookup":
     {
       "from": "tags",
       "localField": "tags",
       "foreignField": "_id",
       "as": "tags"
     }
},
{"$match": {
    "tags.keys": { "$regex": regexFinal, "$options": "i" }
}},
{ "$skip": (page - 1)* limit},
{ "$limit": limit * 1 }
]
    cardResult = mongo.db.cards.aggregate(filtersAdvanced)
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

    filtersAdvanced.pop(-1)
    filtersAdvanced.pop(-1)
    cardCount = mongo.db.cards.aggregate(filtersAdvanced)
    n = 0
    for obj in cardCount:
        n = n + 1

    calcPages = n % limit
    totalPage = 0
    if calcPages != 0:
        totalPage = totalPage + 1
    totalPage = totalPage + math.trunc(n  / limit)
    if n == 0:
        return ({"message":f"Cant find by {api.payload['key']}"}, 400)
    return jsonify({"totalPage":totalPage,"currentPage":page,"total":len(cardList),"cards":cardList})

