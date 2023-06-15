from flask import Flask, g, jsonify
from flask_cors import CORS
from .views.core_view import app_bp
import secrets

def bad_request(e):
    print(e)
    return jsonify({"Error": "A requisição correta precisa ser um objeto JSON."})

def page_not_found(e):
    """Custom error handling for 404"""
    return jsonify({"Error": "Página não encontrada em nosso servidor, verifique sua solicitação por favor."})

def only_json_advice(e):
    return jsonify({
        "msg":"Todas as requisições devem ser realizadas através de um objeto JSON."
        })

def create_app(testing: bool = True):
    app = Flask(__name__)
    CORS(app)
    app.secret_key = secrets.token_hex(16)
    app.register_blueprint(app_bp)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(415, only_json_advice)

    @app.before_request
    def before_request() -> None:
        g.testing = testing

    return app


application = create_app(True)

if __name__ == '__main__':
    application.run(debug=True, hostname='0.0.0.0')
