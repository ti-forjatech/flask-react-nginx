from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required, JWTManager, set_access_cookies, unset_jwt_cookies
from flask import Flask, g, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta, timezone
from modules.config import define_app_secret
import sys, os
import pymysql
pymysql.install_as_MySQLdb()
sys.path.append("/usr/local/lib/python2.7/site-packages")

def bad_request(e):
    return jsonify({"Error": "A requisição correta precisa ser um objeto JSON."})

def page_not_found(e):
    """Custom error handling for 404"""
    return jsonify({"Error": "Página não encontrada em nosso servidor, verifique sua solicitação por favor."})

def only_json_advice(e):
    return jsonify({
        "msg":"Todas as requisições devem ser realizadas através de um objeto JSON."
        })

def not_authorized(e):
    return jsonify({
        "msg":"Não autorizado!."
        })

def signature_verification_failed(e):
    return jsonify({
        "msg":"Token inválido! Verifique sua assinatura."
        })

def create_app(testing: bool = True):
    from .views.core_view import app_bp
    app = Flask(__name__)
    CORS(app)
    jwt = JWTManager(app)
    app = define_app_secret(app)
    app.register_blueprint(app_bp)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(401, not_authorized)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(415, only_json_advice)
    app.register_error_handler(422, signature_verification_failed)

    
    @app.before_request
    def before_request() -> None:
        g.testing = testing
    
    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=5))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            return response
    
    return app

application = create_app(True)

if __name__ == '__main__':
    application.run(host="0.0.0.0")
