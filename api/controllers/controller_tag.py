from flask import Flask, jsonify, Response
from flask_restx import Resource
from server import server
from services.service_tag import *

app, api, mongo = server.app, server.api, server.mongo

class TagClass(Resource):


    def get(self,tag_id = None):
      if tag_id == None:
        tags = getAllTags()
      else:
        tags = getOneTag(tag_id)
      if tags is not False:
        return tags
      else:
        return ({"message":"Database is empty."}, 400)


    def post(self):
        req = api.payload
        if insertTag(req):
          return ({"message":"Tag inserted successfully"}, 201)
        else:
          return ({"message":"Tag cant be inserted"}, 400)


    def delete(self, tag_id):
        if deleteTag(tag_id):
          return ({"message":"Tag deleted successfully"}, 200)
        else:
          return ({"message":"Tag cant be deleted"}, 400)


    def put(self, tag_id):
        req = api.payload
        if updateTag(req, tag_id):
          return ({"message":"Tag updated successfully"}, 200)
        else:
          return ({"message":"Tag cant be updated"}, 400)



api.add_resource(TagClass, '/tags/<tag_id>')
api.add_resource(TagClass, '/tags')