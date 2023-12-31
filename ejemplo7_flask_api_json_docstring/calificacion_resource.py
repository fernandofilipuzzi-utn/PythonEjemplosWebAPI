from flask import jsonify
from flask_restful import Resource, request
import random

class CalificacionResource(Resource):
    def post(self):
        """
        post endpoint
        ---
        tags:
          - flast restful apis
        parameters:
          - name: data
            in: body
            description: datos
            required: false
            type: object
            example: ["str1", "str2", "str3"]
            schematic:
              type: array
              items:
                type: string
              
        responses:
          200:
            description: Lista de usuarios en formato JSON.
        """
        data = request.get_json()

        return jsonify(data)
    
    
    def calcular_puntaje(self, mensaje):
        return random.randint(1, 5)
