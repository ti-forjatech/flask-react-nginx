from flask import Blueprint, jsonify, request
from sqlalchemy import text

notas_bp = Blueprint("notas", __name__, url_prefix="/notas")

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
@notas_bp.post("/inserir")
def insert_nota():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir uma nova nota.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados da novo nota a ser cadastrada."})

# Read all
@notas_bp.get("/listar")
def get_notas():
    return jsonify({
        "method":"GET",
        "acao":"Listar todas as notas.",
        "data":lista
    })

# Read
@notas_bp.get("/buscar")
def get_nota():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar a nota de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@notas_bp.post("/atualizar")
def update_nota():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar a nota de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@notas_bp.post("/remover")
def remove_nota():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover a nota de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})