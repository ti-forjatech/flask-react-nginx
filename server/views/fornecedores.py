from flask import Blueprint, jsonify, request
from sqlalchemy import text

fornecedores_bp = Blueprint("fornecedores", __name__, url_prefix="/fornecedores")

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
@fornecedores_bp.post("/inserir")
def insert_fornecedor():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo fornecedor.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo fornecedor a ser cadastrado."})

# Read all
@fornecedores_bp.get("/listar")
def get_fornecedores():
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os fornecedores.",
        "data":lista
    })

# Read
@fornecedores_bp.get("/buscar")
def get_fornecedor():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar o fornecedor de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@fornecedores_bp.post("/atualizar")
def update_fornecedor():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o fornecedor de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@fornecedores_bp.post("/remover")
def remove_fornecedor():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o fornecedor de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})