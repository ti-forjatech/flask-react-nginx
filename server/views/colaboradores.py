from flask import Blueprint, jsonify, request

colaboradores_bp = Blueprint("colaboradores", __name__, url_prefix="/colaboradores")

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
@colaboradores_bp.post("/inserir")
def insert_colaborador():
    lista_length = len(lista)
    json = request.get_json()
    if json != {}:
        if 'name' in json:
            json['id'] = lista_length + 1
            lista.append(json)
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo colaborador.",
                "data":json
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo colaborador a ser cadastrado."})

# Read all
@colaboradores_bp.get("/listar")
def get_colaboradores():
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os colaboradores.",
        "data":lista
    })

# Read
@colaboradores_bp.get("/buscar")
def get_colaborador():
    data = request.get_json()

    if 'id' in data:
        for register in lista:
            if register['id'] == data['id']:
                return jsonify({
                    "method":"GET",
                    "acao":f"Buscar a colaborador de ID {data['id']}.",
                    "data":register
                })
        return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@colaboradores_bp.post("/atualizar")
def update_colaborador():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:
            for register in lista:
                if register['id'] == data['id']:
                    register['name'] = data['data']['name']
                    print(register)
                    return jsonify({
                        "method":"POST",
                        "acao":f"Atualizar o colaborador de ID {data['id']}.",
                        "data":data
                    })
        return jsonify({"msg":"Insira os dados."})
    return jsonify({"msg":"Insira um ID."})

# Remove
@colaboradores_bp.post("/remover")
def remove_colaborador():
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o colaborador de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})

@colaboradores_bp.errorhandler(415)
def only_json_advice(error):
    return jsonify({
        "msg":"Envie os dados em formato JSON."
        })