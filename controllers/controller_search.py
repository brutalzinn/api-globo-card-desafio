from flask.helpers import make_response
from flask_restx import fields

from server import server
from flask_restx import Resource
from services.service_search import search
app, api = server.app, server.api

body_fields = api.model('Busca', {
    'key': fields.String(description='Nome da tag', required=True,discriminator=True, enum=["nome da tag"]),
})

class SearchClass(Resource):
    @api.doc(body=body_fields,params={'limit': 'Máximo de itens por página','page':'Número da página'})
    def post(self,page,limit):
        return make_response(search(page,limit),200)

