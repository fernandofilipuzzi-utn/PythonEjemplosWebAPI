from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_restful import Api
from hello_world_resource import HelloWorld
from user_resource import UserResource  # Importa la clase UserResource

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

# agregando recursos en la API
api.add_resource(UserResource, '/usuarios')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()
