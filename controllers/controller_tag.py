from flask_restx import Resource, fields
from server import server
from services.service_tag import *
from models.models_tags import Tag


app, api,  = server.app, server.api


tag_body_field = api.model('Tags', {
    'name': fields.String(description='Nome da tag', required=True, enum=["Nome da tag"])
})
class tag_class_extra(Resource):
    @api.doc(params={'tag_id': 'Identificador único'})
    def get(self,tag_id):
        tags = getOneTag(tag_id)
        if tags is not False:
          return tags
        else:
          return ({"message":"Database is empty."}, 400)
class tag_class(Resource):
    def get(self):
      tags = getAllTags()
      if tags is not False:
        return tags
      else:
        return ({"message":"Database is empty."}, 400)

    @api.doc(body=tag_body_field,params={'tag_id': 'Identificador único'})
    def post(self):
        req = api.payload
        tag = Tag(req)
        if not tag.validate():
          return ({"message":"Invalid input"}, 400)
        if insertTag(req):
          return ({"message":"Tag inserted successfully"}, 201)
        else:
          return ({"message":"Tag cant be inserted"}, 400)

    @api.doc(params={'tag_id': 'Identificador único'})
    def delete(self, tag_id):
        if deleteTag(tag_id):
          return ({"message":"Tag deleted successfully"}, 200)
        else:
          return ({"message":"Tag cant be deleted"}, 400)

    @api.doc(body=tag_body_field,params={'tag_id': 'Identificador único'})
    def put(self, tag_id):
        req = api.payload
        tag = Tag(req)
        if not tag.validate():
          return ({"message":"Invalid input"}, 400)
        if updateTag(req, tag_id):
          return ({"message":"Tag updated successfully"}, 200)
        else:
          return ({"message":"Tag cant be updated"}, 400)