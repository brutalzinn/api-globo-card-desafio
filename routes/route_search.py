from server import server
from controllers.controller_search import *

app, api, mongo = server.app, server.api, server.mongo

#ADVANCED SEARCH ROUTE WITH PAGINATION

tag_search = api.namespace('search', description='Rota de busca por tags')
tag_search.add_resource(SearchClass, '/<page>/<limit>', methods=["POST"])
