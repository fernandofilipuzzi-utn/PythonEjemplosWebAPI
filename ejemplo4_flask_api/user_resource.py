# user_resource.py
from flask_restful import Resource

class UserResource(Resource):
    def get(self):
        """
        Endpoint para obtener todos los usuarios.
        ---
        responses:
          200:
            description: Lista de usuarios.
            schema:
              type: array
              items:
                $ref: '#/definitions/Usuario'
        """
        # Lista de usuarios directamente en la clase UserResource
        usuarios = [
            {"id": 1, "nombre": "Juan", "apellido": "Pérez"},
            {"id": 2, "nombre": "María", "apellido": "Gómez"}
        ]
        return usuarios
