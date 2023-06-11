from flask import Flask, g, jsonify
from flask_cors import CORS
from .views.core_view import app_bp

def page_not_found(e):
    """Custom error handling for 404"""
    return jsonify({"error": "página não encontrada"})


def create_app(testing: bool = True):
    app = Flask(__name__)
    CORS(app)
    app.secret_key = 'random secret key'
    app.register_blueprint(app_bp)
    app.register_error_handler(404, page_not_found)

    @app.before_request
    def before_request() -> None:
        g.testing = testing

    return app


application = create_app(False)

if __name__ == '__main__':
    application.run(debug=True, hostname='0.0.0.0')
