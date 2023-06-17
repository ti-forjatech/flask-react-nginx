import bcrypt
import secrets
from datetime import timedelta
from dotenv import dotenv_values

config = dotenv_values(".env")

def define_app_secret(app):
    appconfig_data:str = ""

    with open(".env","r") as env:
        appconfig_data = env.read()

    variavel  = secrets.token_hex(16)
    new_appconfig_data = appconfig_data.replace("SECRET_KEY=None", f"SECRET_KEY={variavel}")

    with open('.env', 'w+') as appconfig:
        appconfig.write(new_appconfig_data)
    
    app.secret_key = config['SECRET_KEY']
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_SECRET_KEY"] = config['SECRET_KEY']

    return app