from flask import Blueprint, jsonify, request
from sqlalchemy import text
from modules.connection import engine
from modules.models import Colaborador
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import get_jwt_identity, jwt_required

colaboradores_bp = Blueprint("colaboradores", __name__, url_prefix="/colaboradores")
Session = sessionmaker(bind=engine)

# Create ok
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
                "new_colab_id": result,
                "current_user":current_user
            })
        
# Read all ok
@colaboradores_bp.get("/listar")
@jwt_required()
def get_colaboradores():
    current_user = get_jwt_identity()
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

    if user_list == []:
        return jsonify({"msg":"Não há colaboradores cadastrados."})
    
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os colaboradores.",
        "data":user_list,
        "current_user":current_user
    })

# Read ok
@colaboradores_bp.get("/buscar")
@jwt_required()
def get_colaborador():
    current_user = get_jwt_identity()
    data = request.get_json()

    if not 'colab_id' in data:
        return jsonify({"msg":"Insira uma chave 'colab_id' e atribua um valor do tipo 'int'."})
    
    with Session() as session:
        result = session.query(Colaborador).where(Colaborador.colab_id == data['colab_id']).one()
        if data['colab_id'] == result.colab_id:
            user_composition = {
                "registro":result.registro,
                "colab_id":result.colab_id,
                "colab_matricula":result.colab_matricula,
                "colab_nome":result.colab_nome,
                "colab_nascimento":result.colab_nascimento,
                "colab_cpf":result.colab_cpf,
                "colab_rg":result.colab_rg,
                "colab_est_civil":result.colab_est_civil,
                "colab_naturalidade":result.colab_naturalidade,
                "end_id":result.end_id,
                "colab_fone":result.colab_fone,
                "colab_celular":result.colab_celular,
                "colab_escolaridade":result.colab_escolaridade,
                "cargo_id":result.cargo_id,
                "colab_admissao":result.colab_admissao,
                "colab_email":result.colab_email,
                "colab_centro_custo":result.colab_centro_custo,
                "colab_salario":result.colab_salario,
                "colab_status":result.colab_status,
                "base_id":result.base_id

            }
            
            return jsonify(user_composition)

# Update ok
@colaboradores_bp.post("/atualizar")
@jwt_required()
def update_colaborador():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['colab_id', 'colab_matricula', 'colab_nome', 'colab_cpf', 'colab_login']

    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})

    with Session() as session:
        session.query(Colaborador).filter(Colaborador.colab_id == data['colab_id']).update(data)
        session.commit()
        return jsonify({"msg":"Colaborador atualizado com sucesso!"})
    
# Remove ok
@colaboradores_bp.post("/remover")
@jwt_required()
def remove_colaborador():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['colab_id']

    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
    
    with Session() as session:
        session.query(Colaborador).filter(Colaborador.colab_id == data['colab_id']).delete()
        session.commit()
        return jsonify({"msg":"Colaborador removido com sucesso!"})