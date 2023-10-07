from flask import Flask, jsonify
from flask_swagger import swagger

app = Flask(__name__)

@app.route('/swagger')
def get_swagger():
    swag = swagger(app)
    swag['info']['version'] = '1.0'
    swag['info']['title'] = 'API Swagger'
    return jsonify(swag)

if __name__ == '__main__':
    app.run(port=5000)
