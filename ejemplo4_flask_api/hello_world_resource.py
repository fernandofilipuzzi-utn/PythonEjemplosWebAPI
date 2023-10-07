# hello_world_resource.py
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        """
        Endpoint para obtener un saludo.
        ---
        responses:
          200:
            description: Saludo exitoso.
            schema:
              type: object
              properties:
                message:
                  type: string
        """
        return {'message': 'Hello, World!'}
