from flask import Blueprint, Response, jsonify, request

app_bp = Blueprint("app", __name__, url_prefix="/app")

@app_bp.get("/data")
def get_data() -> Response:
    data = {
        "api_name":"Rio Service API",
        "api_version":"2.0.0",
        "api_dev_start_date":"09/07/2023",
        "api_author":"Thyéz de Oliveira Monteiro",
        "api_description":"Core API da rio Service."
    }
    return jsonify(data)

@app_bp.post("/login")
def try_to_login():
    is_user_logged_in = False
    json = request.get_json(True)
    login = json['login']
    senha = json['password']
    json.pop('login')
    json.pop('password')
    if login == 'cyberocelot':
        login_ok = True
        if senha == '6ullets':
            senha_ok = True
            if login_ok and senha_ok:
                is_user_logged_in = True
                json["user_logged_in"] = is_user_logged_in
                return jsonify(json)
        json["user_logged_in"] = is_user_logged_in
        json["Erro"] = "A senha digitada nao foi aceita!"
        return jsonify(json)
    json["user_logged_in"] = is_user_logged_in
    json["Erro"] = "O login digitado nao consta em nossa base."
    return jsonify(json)