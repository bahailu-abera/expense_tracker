from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
CORS(app, origins="0.0.0.0")

api_host = getenv('EXPENSE_APP_API_HOST', '0.0.0.0')
api_port = getenv('EXPENSE_APP_API_PORT', '5000')

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Expense Tracker API'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


@app.teardown_appcontext
def teardown(exception):
    """ Commit changes in database """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    resp = {
        'error': 'Not found'
    }
    return jsonify(resp), 404

if __name__ == '__main__':
    app.run(host=api_host, port=int(api_port), threaded=True)
