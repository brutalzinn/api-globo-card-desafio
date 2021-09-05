from server import server
from controllers.controller_tag import *
app, api = server.app, server.api

#TAG ROUTE TO MANAGE TAGS
tag_route = api.namespace('tags', description='Rotas de tags')
tag_route.add_resource(TagClass, '/<tag_id>', methods=["GET","DELETE","PUT"])
tag_route.add_resource(TagClass, '', methods=["POST","GET"])

