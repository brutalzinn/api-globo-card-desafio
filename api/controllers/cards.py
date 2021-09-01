from flask import Flask
from flask_restx import Resource
from server import server



app, api = server.app, server.api

card_teste = [{
  "id": 0,
  "texto": 'texto do card',
  "data_criacao":'data',
  "data_modificacao":'data update',
  "tags":['tag1','tag2']
},
{
  "id": 1,
  "texto": 'texto do card 1',
  "data_criacao":'data 1 ',
  "data_modificacao":'data update 1',
  "tags":['tag3','tag4']
}]
@api.route('/teste')
class CardClass(Resource):
    def get(self, ):
        return card_teste
