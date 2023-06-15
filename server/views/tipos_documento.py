from flask import Blueprint, jsonify, request
from sqlalchemy import text

tipos_documento_bp = Blueprint("tipos_documento", __name__, url_prefix="/tipos_documento")

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
@tipos_documento_bp.post("/inserir")
def insert_tipo_documento():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo tipo de documento.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo tipo de documento a ser cadastrado."})

# Read all
@tipos_documento_bp.get("/listar")
def get_tipos_documento():
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os tipos de documento.",
        "data":lista
    })

# Read
@tipos_documento_bp.get("/buscar")
def get_tipo_documento():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar o tipo de documento de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@tipos_documento_bp.post("/atualizar")
def update_tipo_documento():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o tipo de documento de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@tipos_documento_bp.post("/remover")
def remove_tipo_documento():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o tipo de documento de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})