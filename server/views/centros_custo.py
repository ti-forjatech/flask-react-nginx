from flask import Blueprint, jsonify, request
from sqlalchemy import text

centros_custo_bp = Blueprint("centros_custo", __name__, url_prefix="/centros_custo")

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
@centros_custo_bp.post("/inserir")
def insert_centro_custo():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo centro de custo.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo centro de custo a ser cadastrado."})

# Read all
@centros_custo_bp.get("/listar")
def get_centros_custo():
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os centros de custo.",
        "data":lista
    })

# Read
@centros_custo_bp.get("/buscar")
def get_centro_custo():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar o centro de custo de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@centros_custo_bp.post("/atualizar")
def update_centro_custo():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o centro de custo de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@centros_custo_bp.post("/remover")
def remove_centro_custo():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o centro_custo de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})
