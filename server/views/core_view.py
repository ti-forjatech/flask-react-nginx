from flask import Blueprint, Response, jsonify, request
from .colaboradores import colaboradores_bp
from .cargos import cargos_bp
from .bases import bases_bp
from .fornecedores import fornecedores_bp
from .notas import notas_bp
from .cotacoes import cotacoes_bp
from .estoque import estoque_bp

# Registro da Blueprint do app e da versao 2 da API
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

@app_bp.get("/data")
def get_data() -> Response:
    data = {
        "api_name":"Rio Services core API",
        "api_version":"2.0.0",
        "api_dev_start_date":"09/07/2023",
        "api_author":"Forjatech Soluções Tecnológicas (Thyéz de Oliveira Monteiro)",
        "api_description":"API central da Rio Services. Esta API provê recursos computacionais de alta performance e escalabilidade para o recolhimento, armazenamento adequado, operaçoes e proteção dos dados da empresa."
    }
    return jsonify(data)

@app_bp.post("/login")
def try_to_login():
    is_user_logged_in = False
    json = request.get_json(True)
    login = None
    senha = None
    login = json['login']
    senha = json['password']
    json.pop('login')
    json.pop('password')
    if login != "":
        if senha != "":
            if login == 'cyberocelot':
                login_ok = True
                if senha == '6ullets':
                    senha_ok = True
                    if login_ok and senha_ok:
                        is_user_logged_in = True
                        json["user_logged_in"] = is_user_logged_in
                        return jsonify(json)
                json["user_logged_in"] = is_user_logged_in
                json["Erro"] = "A senha digitada nao foi registrada por esse usuario!"
                return jsonify(json)
            json["user_logged_in"] = is_user_logged_in
            json["Erro"] = "O login digitado nao consta em nossa base."
            return jsonify(json)
        json["user_logged_in"] = is_user_logged_in
        json["Erro"] = "Preencha a senha."
        return jsonify(json)
    json["user_logged_in"] = is_user_logged_in
    json["Erro"] = "Preencha o login!"
    return jsonify(json)
