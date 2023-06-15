from flask import Blueprint, jsonify, request
from sqlalchemy import text

sub_centros_custo_bp = Blueprint("sub_centros_custo", __name__, url_prefix="/sub_centros_custo")

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
@sub_centros_custo_bp.post("/inserir")
def insert_sub_centro_custo():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo sub centro de custo.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo sub centro de custo a ser cadastrado."})

# Read all
@sub_centros_custo_bp.get("/listar")
def get_sub_centros_custo():
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os sub centros de custo.",
        "data":lista
    })

# Read
@sub_centros_custo_bp.get("/buscar")
def get_sub_centro_custo():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar o sub centro de custo de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@sub_centros_custo_bp.post("/atualizar")
def update_sub_centro_custo():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o sub centro de custo de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@sub_centros_custo_bp.post("/remover")
def remove_sub_centro_custo():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o sub centro custo de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})