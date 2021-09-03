from server import server
from controllers.controller_tag import *
app, api = server.app, server.api

api.add_resource(TagClass, '/tags/<tag_id>')
api.add_resource(TagClass, '/tags')

