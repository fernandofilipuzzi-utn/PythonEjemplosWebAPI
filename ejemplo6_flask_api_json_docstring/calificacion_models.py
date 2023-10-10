#calificacion_models.py
from flask_restful import fields

item_model = {
    'id': fields.Integer,
    'mensaje': fields.String
}

input_model = {
    'data': fields.List(fields.Nested(item_model))
}
