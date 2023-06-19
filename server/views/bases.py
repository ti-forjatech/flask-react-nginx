from flask import Blueprint, jsonify, request
from sqlalchemy import text
from modules.connection import engine
from modules.models import Base
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import get_jwt_identity, jwt_required

bases_bp = Blueprint("bases", __name__, url_prefix="/bases")
Session = sessionmaker(bind=engine)

# Create ok
@bases_bp.post("/inserir")
@jwt_required()
def insert_base():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['base_nome','base_desc']

    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
    
    if data == {}:
        return jsonify({"msg":"Insira os dados da nova base a ser cadastrada."})
    else:
        with Session() as session:
            base = Base(**data)
            result = session.add(base)
            session.commit()

            return jsonify({
                "msg":"Base inserida com sucesso!",
                "base_inserted":True,
                "new_base_id": result,
                "current_user":current_user
            })

# Read all ok
@bases_bp.get("/listar")
@jwt_required()
def get_bases():
    current_user = get_jwt_identity()
    base_list = []
    with Session() as session:
        result = session.query(Base).all()
        for row in result:
            base_composition = {
                "base_id":row.base_id,
                "base_name":row.base_nome,
                "base_desc":row.base_desc
            }
            base_list.append(base_composition)

    if base_list == []:
        return jsonify({"msg":"Não há bases cadastradas."})

    return jsonify({
        "method":"GET",
        "acao":"Listar todas as bases.",
        "data":base_list,
        "current_user":current_user
    })

# Read ok
@bases_bp.get("/buscar")
@jwt_required()
def get_base():
    current_user = get_jwt_identity()
    data = request.get_json()

    if not 'base_id' in data:
        return jsonify({"msg":"Insira a chave 'base_id' e atribua um valor do tipo 'int'."})
    
    with Session() as session:
        result = session.query(Base).filter(Base.base_id == data['base_id']).first()

        base_composition = {
            "base_id":result.base_id,
            "base_name":result.base_nome,
            "base_desc":result.base_desc
        }

        return jsonify({
            "method":"GET",
            "acao":f"Buscar a base de ID {data['base_id']}.",
            "data":base_composition,
            "current_user":current_user
        })

# Update ok
@bases_bp.post("/atualizar")
@jwt_required()
def update_base():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['base_id','base_nome','base_desc']
    
    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
    
    if data == {}:
        return jsonify({"msg":"Insira os dados da base a ser atualizada."})
    
    with Session() as session:
        session.query(Base).filter(Base.base_id == data['base_id']).update(data)
        session.commit()

        return jsonify({
            "method":"POST",
            "acao":f"Atualizar a base de ID {data['base_id']}.",
            "data":data,
            "current_user":current_user
        })

# Remove ok
@bases_bp.post("/remover")
@jwt_required()
def remove_base():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['base_id']

    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
    
    if data == {}:
        return jsonify({"msg":"Insira os dados da base a ser removida."})
    
    with Session() as session:
        session.query(Base).filter(Base.base_id == data['base_id']).delete()
        session.commit()

        return jsonify({
            "method":"POST",
            "acao":f"Remover a base de ID {data['base_id']}.",
            "current_user":current_user
        })