from server import server
from controllers.controller_tag import *
app, api = server.app, server.api

#TAG ROUTE TO MANAGE TAGS
tag_route = api.namespace('tags', description='Rotas de tags')
tag_route.add_resource(tag_class_extra, '/<tag_id>', methods=["GET"])
tag_route.add_resource(tag_class, '/<tag_id>', methods=["DELETE","PUT","GET"])
tag_route.add_resource(tag_class, '', methods=["POST","GET"])

