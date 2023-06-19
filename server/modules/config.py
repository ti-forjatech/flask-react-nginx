import secrets, os
from datetime import timedelta

def define_app_secret(app):
    variavel  = secrets.token_hex(16)
    os.environ["APP_SECRET_KEY"] = variavel
    
    app.secret_key = os.environ.get("APP_SECRET_KEY")
    app.config["JWT_SECRET_KEY"] = os.environ.get("APP_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json"]

    return app