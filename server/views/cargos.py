from flask import Blueprint, jsonify, request

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
def insert_cargo():
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
    return jsonify({"msg":"Insira os dados do nova cargo a ser cadastrado."})

# Read all
@cargos_bp.get("/listar")
def get_cargos():
    return jsonify({
        "method":"GET",
        "acao":"Listar todas as cargos.",
        "data":lista
    })

# Read
@cargos_bp.get("/buscar")
def get_cargo():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar a cargo de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@cargos_bp.post("/atualizar")
def update_cargo():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar a cargo de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@cargos_bp.post("/remover")
def remove_cargo():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover a cargo de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})

@cargos_bp.errorhandler(415)
def only_json_advice(error):
    return jsonify({
        "msg":"Envie os dados em formato JSON."
        })