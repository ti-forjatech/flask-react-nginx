from flask import Blueprint, jsonify, request
from sqlalchemy import text
from ..modules.connection import engine
from ..modules.models import Colaborador
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import get_jwt_identity, jwt_required, current_user

colaboradores_bp = Blueprint("colaboradores", __name__, url_prefix="/colaboradores")
Session = sessionmaker(bind=engine)

# Create
@colaboradores_bp.post("/inserir")
@jwt_required()
def insert_colaborador():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['colab_matricula', 'colab_nome', 'colab_cpf', 'colab_login', 'colab_password']
    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
        
    if data == {}:
        return jsonify({"msg":"Insira os dados do novo colaborador a ser cadastrado."})
    else:
        with Session() as session:
            colaborador = Colaborador(**data)
            result = session.add(colaborador)
            session.commit()

            return jsonify({
                "msg":"Usuário inserido com sucesso!",
                "colab_inserted":True,
                "new_colab_id": result
            })
        
# Read all
@colaboradores_bp.get("/listar")
@jwt_required()
def get_colaboradores():
    current_user = get_jwt_identity()
    print("current_user: ", current_user)
    user_list = []
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
            user_list.append(user_composition)

    return jsonify({
        "method":"GET",
        "acao":"Listar todos os colaboradores.",
        "data":user_list,
        "logged_user":current_user
    })

# Read
@colaboradores_bp.get("/buscar")
@jwt_required()
def get_colaborador():
    current_user = get_jwt_identity()
    data = request.get_json()
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
@jwt_required()
def update_colaborador():
    current_user = get_jwt_identity()
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
@jwt_required()
def remove_colaborador():
    current_user = get_jwt_identity()
    data = request.get_json()
    if 'id' in data:
        del lista[data['id'] - 1]
        return jsonify({
            "method":"POST",
            "acao":f"Remover o colaborador de ID {data['id']}.",
        })
    return jsonify({"msg":"Insira um ID."})