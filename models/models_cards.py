from flask_restx import fields
from server import *

card_model = server.api.model('Cards', {
    'name': fields.String,
})