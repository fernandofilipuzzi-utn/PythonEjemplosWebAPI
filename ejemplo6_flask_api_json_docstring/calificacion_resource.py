from flask import jsonify
from flask_restful import Resource, request
import random

from calificacion_models import input_model, item_model

class CalificacionResource(Resource):
    def get(self):
        """
        post endpoint
        ---
        tags:
          - flast restful apis
        parameters:
          - name: data
            in: query
            description: datos
            required: false
            type: string
        responses:
          200:
            description: Lista de usuarios en formato JSON.
        """
        data= request.args.get("data")

        calificaciones=[]
        calificaciones.append(data)
        return jsonify(calificaciones)
    
    
    def calcular_puntaje(self, mensaje):
        return random.randint(1, 5)
