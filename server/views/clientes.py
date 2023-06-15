from flask import Blueprint, jsonify, request
from sqlalchemy import text

clientes_bp = Blueprint("clientes", __name__, url_prefix="/clientes")

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
@clientes_bp.post("/inserir")
def insert_cliente():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo cliente.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo cliente a ser cadastrado."})

# Read all
@clientes_bp.get("/listar")
def get_clientes():
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os clientes.",
        "data":lista
    })

# Read
@clientes_bp.get("/buscar")
def get_cliente():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar o cliente de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@clientes_bp.post("/atualizar")
def update_cliente():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o cliente de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@clientes_bp.post("/remover")
def remove_cliente():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o cliente de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})