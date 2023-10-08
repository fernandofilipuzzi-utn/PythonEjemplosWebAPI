from flask import jsonify
from flask_restful import Resource

class UserResource(Resource):
    def get(self):
        """
        Endpoint para obtener todos los usuarios.
        ---
        responses:
          200:
            description: Lista de usuarios en formato JSON.
        """
        usuarios = [
            {"id": 1, "nombre": "Juan", "apellido": "Pérez"},
            {"id": 2, "nombre": "María", "apellido": "Gómez"}
        ]
        # Devuelve la lista de usuarios como JSON
        return jsonify(usuarios)
