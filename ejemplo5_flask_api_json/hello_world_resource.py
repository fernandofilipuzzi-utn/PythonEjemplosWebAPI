from flask import jsonify
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        """
        Endpoint para obtener un saludo.
        ---
        responses:
          200:
            description: Saludo exitoso en formato JSON.
        """
        saludo = {'message': 'Hello, World!'}
        # Devuelve el saludo como JSON
        return jsonify(saludo)
