from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy import text

cargos_bp = Blueprint("cargos", __name__, url_prefix="/cargos")

# CRUD #
# Lista de teste
lista = [
    {
        "id":1,
        "name": "Test1"
    },
    {
        "id":2,
        "name": "Test2"
    },
    {
        "id":3,
        "name": "Test3"
    },
]

# Create
@cargos_bp.post("/inserir")
@jwt_required()
def insert_cargo():
    current_user = get_jwt_identity()
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo cargo.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo cargo a ser cadastrado."})

# Read all
@cargos_bp.get("/listar")
@jwt_required()
def get_cargos():
    current_user = get_jwt_identity()
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os cargos.",
        "data":lista
    })

# Read
@cargos_bp.get("/buscar")
@jwt_required()
def get_cargo():
    current_user = get_jwt_identity()
    data = request.get_json()
    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar o cargo de ID {data['id']}.",
                    "data":register,
                    "logged_user":current_user
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@cargos_bp.post("/atualizar")
@jwt_required()
def update_cargo():
    current_user = get_jwt_identity()
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o cargo de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@cargos_bp.post("/remover")
@jwt_required()
def remove_cargo():
    current_user = get_jwt_identity()
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o cargo de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})