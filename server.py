from flask import Flask
from flask_cors import CORS
from flask_restx import Resource, Api
from flask_pymongo import PyMongo
import os

from flask_restx.namespace import Namespace

production = int(os.environ['PRODUCTION'])
class Server():
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        if production == 0:
            self.app.config["MONGO_URI"] = f"mongodb://{os.environ['MONGO_HOST']}:27017/{os.environ['MONGO_DB_NAME']}"
        else:
            self.app.config["MONGO_URI"] = os.environ['MONGO_DB_ATLAS']
        self.api = Api(self.app,title='GloboCardAPI - Desafio',
            version='1.0',
            default ='Rotas',
            default_label='Rotas para teste',
            description='repositório original: https://github.com/brutalzinn/api-globo-card-desafio')

        self.mongo = PyMongo(self.app)

    def run(self):
        self.app.run(debug=True,host="0.0.0.0")

server = Server()