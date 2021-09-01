from flask import Flask
from flask_restx import Resource, Api

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def run(self):
        self.app.run(debug=True,host="0.0.0.0")

server = Server()