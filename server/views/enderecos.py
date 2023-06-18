from flask import Blueprint, jsonify, request
from sqlalchemy import text
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..modules.connection import engine
from ..modules.models import Endereco
from sqlalchemy.orm import sessionmaker

enderecos_bp = Blueprint("enderecos", __name__, url_prefix="/enderecos")
Session = sessionmaker(bind=engine)

# Create ok
@enderecos_bp.post("/inserir")
@jwt_required()
def insert_endereco():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['end_tipo','end_cep', 'end_numero', 'end_referencia']

    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
    
    if data == {}:
        return jsonify({"msg":"Insira os dados do novo endereco a ser cadastrado."})
    
    with Session() as session:
        endereco = Endereco(**data)
        cep = endereco.get_end_from_viacep()
        result = session.add(endereco)
        session.commit()

        return jsonify({
            "msg":"Endereco inserido com sucesso!",
            "endereco_inserted":True,
            "new_end": cep,
            "current_user":current_user
        })

# Read all ok
@enderecos_bp.get("/listar")
@jwt_required()
def get_enderecos():
    current_user = get_jwt_identity()
    lista_enderecos = []

    with Session() as session:
        enderecos = session.query(Endereco).all()
        for endereco in enderecos:
            endereco_composition = {
                "end_id":endereco.end_id,
                "end_tipo":endereco.end_tipo,
                "end_cep":endereco.end_cep,
                "end_logradouro":endereco.end_logradouro,
                "end_numero":endereco.end_numero,
                "end_bairro":endereco.end_bairro,
                "end_cidade":endereco.end_cidade,
                "end_uf":endereco.end_uf,
                "end_referencia":endereco.end_referencia
            }

            lista_enderecos.append(endereco_composition)
    
    if lista_enderecos == []:
        return jsonify({"msg":"Nenhum endereco cadastrado."})
    
    return jsonify({
        "method":"GET",
        "acao":"Listar todos os enderecos.",
        "data":lista_enderecos,
        "current_user":current_user
    })

# Read ok
@enderecos_bp.get("/buscar")
@jwt_required()
def get_endereco():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['end_id']

    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
        
    if data == {}:
        return jsonify({"msg":"Insira os dados do endereco a ser buscado."})
    
    with Session() as session:
        endereco = session.query(Endereco).filter_by(end_id=data['end_id']).first()
        endereco_composition = {
            "end_id":endereco.end_id,
            "end_tipo":endereco.end_tipo,
            "end_cep":endereco.end_cep,
            "end_logradouro":endereco.end_logradouro,
            "end_numero":endereco.end_numero,
            "end_bairro":endereco.end_bairro,
            "end_cidade":endereco.end_cidade,
            "end_uf":endereco.end_uf,
            "end_referencia":endereco.end_referencia
        }

        return jsonify({
            "method":"GET",
            "acao":f"Buscar o endereco de ID {data['end_id']}.",
            "endereco":endereco_composition,
            "current_user":current_user
        })

# Update ok
@enderecos_bp.post("/atualizar")
@jwt_required()
def update_endereco():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['end_id','end_tipo','end_cep', 'end_numero', 'end_referencia']

    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
        
    if data == {}:
        return jsonify({"msg":"Insira os dados do endereco a ser atualizado."})
    
    with Session() as session:
        current_endereco = session.query(Endereco).filter_by(end_id=data['end_id']).first()
        current_endereco.end_cep = data['end_cep']
        new_end = current_endereco.get_end_from_viacep()
        current_endereco.end_tipo = data['end_tipo']
        current_endereco.end_numero = data['end_numero']
        current_endereco.end_referencia = data['end_referencia']
        session.commit()

        return jsonify({
            "method":"POST",
            "acao":f"Atualizar o endereco de ID {data['end_id']}.",
            "new_data":new_end,
            "current_user":current_user
        })

# Remove ok
@enderecos_bp.post("/remover")
@jwt_required()
def remove_endereco():
    current_user = get_jwt_identity()
    data = request.get_json()
    required_fields = ['end_id']

    for field in required_fields:
        if not field in data:
            return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})
        
    if data == {}:
        return jsonify({"msg":"Insira os dados do endereco a ser removido."})

    with Session() as session:
        endereco = session.query(Endereco).filter_by(end_id=data['end_id']).first()
        session.delete(endereco)
        session.commit()

        return jsonify({
            "method":"POST",
            "acao":f"Remover o endereco de ID {data['end_id']}.",
        })