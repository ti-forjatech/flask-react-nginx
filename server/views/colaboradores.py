from flask import Blueprint, jsonify, request
from sqlalchemy import text
from ..modules.connection import engine

colaboradores_bp = Blueprint("colaboradores", __name__, url_prefix="/colaboradores")

# CRUD #

# Create
@colaboradores_bp.post("/inserir")
def insert_colaborador():
    data = request.get_json()
    if data != {}:
        if 'name' in data:
            data['user_inserted'] = True
            return jsonify({
                "method":"POST",
                "acao":f"Inserir um novo colaborador.",
                "data":data
            })
        return jsonify({"msg":"Insira uma chave 'name' ."})
    return jsonify({"msg":"Insira os dados do novo colaborador a ser cadastrado."})

# Read all
@colaboradores_bp.get("/listar")
def get_colaboradores():
    lista = []
    with engine.connect() as connection:
        result = connection.execute(text("select * from tb_colaboradores"))
        for row in result:
            user_composition = {
                "registro":row[0],
                "colab_id":row[1],
                "colab_matricula":row[2],
                "colab_nome":row[3],
                "colab_nascimento":row[4],
                "colab_cpf":row[5],
                "colab_rg":row[6],
                "colab_est_civil":row[7],
                "colab_naturalidade":row[8],
                "end_id":row[9],
                "colab_fone":row[10],
                "colab_celular":row[11],
                "colab_escolaridade":row[12],
                "cargo_id":row[13],
                "colab_admissao":row[15],
                "colab_email":row[16],
                "colab_centro_custo":row[17],
                "colab_salario":row[18],
                "colab_status":row[19],
                "base_id":row[20],
            }
            lista.append(user_composition)

    return jsonify({
        "method":"GET",
        "acao":"Listar todos os colaboradores.",
        "data":lista
    })

# Read
@colaboradores_bp.get("/buscar")
def get_colaborador():
    data = request.get_json()

    print(data)

    if 'id' in data:
        with engine.connect() as connection:
            result = connection.execute(text(f"select * from tb_colaboradores where colab_id={data['id']}"))
            for row in result:
                if data['id'] == row[1]:
                    user_composition = {
                        "registro":row[0],
                        "colab_id":row[1],
                        "colab_matricula":row[2],
                        "colab_nome":row[3],
                        "colab_nascimento":row[4],
                        "colab_cpf":row[5],
                        "colab_rg":row[6],
                        "colab_est_civil":row[7],
                        "colab_naturalidade":row[8],
                        "end_id":row[9],
                        "colab_fone":row[10],
                        "colab_celular":row[11],
                        "colab_escolaridade":row[12],
                        "cargo_id":row[13],
                        "colab_admissao":row[15],
                        "colab_email":row[16],
                        "colab_centro_custo":row[17],
                        "colab_salario":row[18],
                        "colab_status":row[19],
                        "base_id":row[20],
                    }
                    return jsonify(user_composition)
                return jsonify({"msg":"Insira um ID valido."})
    return jsonify({"msg":"Insira um ID."})

# Update
@colaboradores_bp.post("/atualizar")
def update_colaborador():
    data = request.get_json()
    if 'id' in data:
        if 'data' in data:

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