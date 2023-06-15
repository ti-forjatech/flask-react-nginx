from flask import Blueprint, jsonify, request
from sqlalchemy import text

itens_bp = Blueprint("itens", __name__, url_prefix="/itens")

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
@itens_bp.post("/inserir")
def insert_item():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo item.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo item a ser cadastrado."})

# Read all
@itens_bp.get("/listar")
def get_itens():
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os itens.",
        "data":lista
    })

# Read
@itens_bp.get("/buscar")
def get_item():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar o item de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@itens_bp.post("/atualizar")
def update_item():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o item de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@itens_bp.post("/remover")
def remove_item():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o item de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})