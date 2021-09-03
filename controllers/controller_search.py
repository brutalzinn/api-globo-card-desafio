from bson.objectid import ObjectId
from flask.json import jsonify
from flask_restx import Resource
from flask import Response
from server import server

app, api, mongo = server.app, server.api, server.mongo

@app.route('/search', methods=["POST"])
def search():
    page = 1
    limit = 5
    print('Search hello world')
    keys = api.payload['key'].upper().split(" ")
    regex = ''
    for k in keys:
        regex = f'^{k}|' + regex

    max = len(regex)
    n = 1
    regexFinal = ''
    print(max)

    for l in regex:
        print(l)
        if n != max:
            regexFinal = regexFinal + l
        else:
            break
        n = n + 1
    filters = { "keys": { "$regex": regexFinal, "$options": "i" }}
    print(regexFinal)
    tagsResult = mongo.db.tags.find_one(filters)
    if tagsResult is None:
        return ({"message":f"Cant find by {api.payload['key']}"}, 400)
    filters = [{
   "$lookup":
     {
       "from": "tags",
       "localField": "tags",
       "foreignField": "_id",
       "as": "tags"
     }
},
{ "$skip": (page - 1)* limit},
{ "$limit": limit * 1 },
{"$match": {
    "tags._id": ObjectId(tagsResult['_id'])
}}
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

    return jsonify([cardList])

