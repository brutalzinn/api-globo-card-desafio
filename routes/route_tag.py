from server import server
from controllers.controller_tag import *
app, api = server.app, server.api

#TAG ROUTE TO MANAGE TAGS
api.add_resource(TagClass, '/v1/tags/<tag_id>', methods=['GET'])
api.add_resource(TagClass, '/v1/tags')

