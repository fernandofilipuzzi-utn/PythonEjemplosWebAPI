from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_restful import Api, Resource

app = Flask(__name__)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "swagger",
            "route": "/swagger.json",
            "rule_filter": lambda rule: True,  # Mostrar todas las reglas
            "model_filter": lambda tag: True,  # Mostrar todos los modelos
        }
    ],
    "static_url_path": "/flasgger_static",  # Ruta para los archivos estáticos de Swagger UI
    "swagger_ui": True,  # Habilitar el UI de Swagger
    "specs_route": "/swagger/"  # Ruta para el UI de Swagger
}

Swagger(app, config=swagger_config)

api = Api(app)

# Datos de ejemplo para simular una base de datos
usuarios = [
    {"id": 1, "nombre": "Juan", "apellido": "Pérez"},
    {"id": 2, "nombre": "María", "apellido": "Gómez"}
]

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    """
    Obtener todos los usuarios.
    ---
    responses:
      200:
        description: Lista de usuarios.
        schema:
          type: array
          items:
            $ref: '#/definitions/Usuario'
    """
    return jsonify(usuarios)

# Resto de las rutas...

# Ruta para el endpoint de Swagger
@app.route('/swagger')
def swagger_ui():
    return jsonify(swagger)

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

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
