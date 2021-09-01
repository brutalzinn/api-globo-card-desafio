from flask import Flask
from flask_restx import Resource, Api
from flask_pymongo import PyMongo
import os


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config["MONGO_URI"] = f"mongodb://{os.environ['MONGO_HOST']}:27017/{os.environ['MONGO_DB_NAME']}"
        self.api = Api(self.app)
        self.mongo = PyMongo(self.app)

    def run(self):
        self.app.run(debug=True,host="0.0.0.0")

server = Server()