from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UsuarioResource(Resource):
    def get(self):
        """
        Obtiene la lista de usuarios.

        Este endpoint devuelve una lista de usuarios.

        ---
        responses:
          200:
            description: Lista de usuarios.
          400:
            description: Error en la solicitud.
        """
        usuarios = [
            {"id": 1, "nombre": "Juan", "apellido": "Pérez"},
            {"id": 2, "nombre": "María", "apellido": "Gómez"}
        ]
        return usuarios

api.add_resource(UsuarioResource, '/usuarios')

if __name__ == '__main__':
    app.run(debug=True)
