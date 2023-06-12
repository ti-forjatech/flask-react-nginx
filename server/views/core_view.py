from flask import Blueprint, Response, jsonify, request
from .colaboradores import colaboradores_bp
from .cargos import cargos_bp
from .bases import bases_bp
from .fornecedores import fornecedores_bp
from .notas import notas_bp
from .cotacoes import cotacoes_bp
from .estoque import estoque_bp
from .centros_custo import centros_custo_bp
from .sub_centros_custo import sub_centros_custo_bp
from .clientes import clientes_bp
from .tipos_documento import tipos_documento_bp
from .cargo_acessos import cargo_acessos_bp
from ..auth import users

# criação das Blueprints da API: app e v2
app_bp = Blueprint("app", __name__, url_prefix="/app")
v2_bp = Blueprint("v2", __name__, url_prefix="/v2")

# Registro do v2 no app
app_bp.register_blueprint(v2_bp)

# Registro de todas Blueprints da API V2
v2_bp.register_blueprint(colaboradores_bp)
v2_bp.register_blueprint(cargos_bp)
v2_bp.register_blueprint(bases_bp)
v2_bp.register_blueprint(fornecedores_bp)
v2_bp.register_blueprint(notas_bp)
v2_bp.register_blueprint(cotacoes_bp)
v2_bp.register_blueprint(estoque_bp)
v2_bp.register_blueprint(centros_custo_bp)
v2_bp.register_blueprint(sub_centros_custo_bp)
v2_bp.register_blueprint(tipos_documento_bp)
v2_bp.register_blueprint(cargo_acessos_bp)

@app_bp.get("/data")
def get_data() -> Response:
    data = {
        "api_name":"Rio Services core API",
        "api_version":"2.1.0",
        "api_dev_start_date":"09/07/2023",
        "api_author":"Forjatech Soluções Tecnológicas (Thyéz de Oliveira Monteiro)",
        "api_description":"API central da Rio Services. Esta API provê recursos computacionais de alta performance e escalabilidade para o recolhimento, armazenamento adequado, operaçoes e proteção dos dados da empresa."
    }
    return jsonify(data)

@app_bp.post("/login")
def try_to_login():
    json = request.get_json()
    user_temp = None
    json_ok = None
    is_user_logged_in = False
    login_ok = False
    password_ok = False

    if not 'login' in json:
        json['Error'] = 'Insira a chave "login" e atribua um valor'
    else:
        if not 'password' in json:
            json['Error'] = 'Insira a chave "password" e atribua um valor'
        else:
            json_ok = True

    if json_ok:
        json_login = json['login']
        json_password = json['password']
        json['Erro'] = None
        
        for user in users:
            if user['login'] != json_login:
                json["Erro"] = "O usuário não consta em nossa base de dados."
            else:
                user_temp = user
                login_ok = True

    if user_temp != None and login_ok:
        if user_temp['password'] != json_password:
            json["Erro"] = "A senha inserida não corresponde a um usuario cadastrado!"
        else: password_ok = True

    if login_ok and password_ok:
        json.pop("Erro")
        is_user_logged_in = True
        json["user_logged_in"] = is_user_logged_in
        json["user"] = user_temp
        json.pop("login", None)
        json.pop("password", None)

    return jsonify(json)