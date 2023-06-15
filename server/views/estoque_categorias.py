from flask import Blueprint, jsonify, request
from sqlalchemy import text

categorias_bp = Blueprint("categorias", __name__, url_prefix="/categorias")

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
@categorias_bp.post("/inserir")
def insert_categoria():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir uma nova categoria.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados da nova categoria a ser cadastrada."})

# Read all
@categorias_bp.get("/listar")
def get_categorias():
    return jsonify({
        "method":"GET",
        "acao":"Listar todas as categorias.",
        "data":lista
    })

# Read
@categorias_bp.get("/buscar")
def get_categoria():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar a categoria de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@categorias_bp.post("/atualizar")
def update_categoria():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar a categoria de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@categorias_bp.post("/remover")
def remove_categoria():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover a categoria de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})