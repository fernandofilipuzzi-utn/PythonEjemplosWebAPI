from flask import Flask

# https://discuss.python.org/t/error-importing-mutablemapping-from-collections/29957/2
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping

from flask_restplus import Api, Resource

flask_app = Flask(__name__)

app = Api(app = flask_app)
name_space = app.namespace('main', description='Main APIs')

from flask import Flask
from flask_restplus import Api, Resource

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}

if __name__ == "__main__":
    flask_app.run(debug=True, host='0.0.0.0', port=5000)
