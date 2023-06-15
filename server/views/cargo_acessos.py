from flask import Blueprint, jsonify, request
from sqlalchemy import text

cargo_acessos_bp = Blueprint("cargo_acessos", __name__, url_prefix="/cargo_acessos")

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
@cargo_acessos_bp.post("/inserir")
def insert_cargo_acesso():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo nivel de acesso de cargo.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo nivel de acesso de cargo a ser cadastrado."})

# Read all
@cargo_acessos_bp.get("/listar")
def cargo_acessos():
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os niveis de acesso de cargo.",
        "data":lista
    })

# Read
@cargo_acessos_bp.get("/buscar")
def get_cargo_acesso():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar o nivel de acesso de cargo de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@cargo_acessos_bp.post("/atualizar")
def update_cargo_acesso():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o nivel de acesso de cargo de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@cargo_acessos_bp.post("/remover")
def remove_cargo_acesso():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o sub centro custo de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})