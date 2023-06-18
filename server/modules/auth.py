from flask import Blueprint, jsonify, request
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies
from .connection import engine
from .models import Colaborador
from .cryptopass import decode_pass

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
Session = sessionmaker(bind=engine)

@auth_bp.post('/login')
def login():
    json = request.get_json()
    if not 'data' in json:
        return jsonify({"msg":"Insira uma chave 'data' e atribua um objeto json."})
    else:
        if not type(json['data']) == type(json):
            return jsonify({"msg":"O valor de 'data' deve ser um objeto Json."})
        else:
            if json['data'] == {}:
                return jsonify({"msg":"O objeto 'data' não pode ser vazio."})
            else:
                data = json['data']
                required_fields = ['colab_login', 'colab_password']
                for field in required_fields:
                    if not field in data:
                        return jsonify({"msg":f"Insira uma chave '{field}' e atribua um valor."})

                stmt = select(Colaborador).where(Colaborador.colab_login == data['colab_login'])
                with Session() as session:
                    for row in session.execute(stmt):
                        colab = row[0]
                        password_ok = decode_pass(data['colab_password'], colab.colab_password)
                        if not password_ok:
                            return jsonify({"Erro":"Nao autorizado!"})
                        
                        user_composition = {
                            "registro":colab.registro,
                            "colab_id":colab.colab_id,
                            "colab_matricula":colab.colab_matricula,
                            "colab_nome":colab.colab_nome,
                            "colab_nascimento":colab.colab_nascimento,
                            "colab_cpf":colab.colab_cpf,
                            "colab_rg":colab.colab_rg,
                            "colab_est_civil":colab.colab_est_civil,
                            "colab_naturalidade":colab.colab_naturalidade,
                            "end_id":colab.end_id,
                            "colab_fone":colab.colab_fone,
                            "colab_celular":colab.colab_celular,
                            "colab_escolaridade":colab.colab_escolaridade,
                            "cargo_id":colab.cargo_id,
                            "colab_admissao":colab.colab_admissao,
                            "colab_email":colab.colab_email,
                            "colab_centro_custo":colab.colab_centro_custo,
                            "colab_salario":colab.colab_salario,
                            "colab_status":colab.colab_status,
                            "base_id":colab.base_id,
                            "user_logged_in":True
                        }

                        keys_to_remove = ['registro', 'colab_nascimento', 'colab_rg', 'colab_est_civil', 'colab_naturalidade', 'colab_fone', 'colab_celular', 'colab_escolaridade', 'colab_admissao', 'colab_centro_custo', 'colab_salario', 'colab_status']
                        jwt_prepared_object = {}


                        for key in user_composition:
                            if not key in keys_to_remove:
                                jwt_prepared_object[key] = user_composition[key]

                        access_token = create_access_token(identity=jwt_prepared_object)
                        user_composition['x-JWT'] = access_token
                        response = jsonify(user_composition)
                        set_access_cookies(response, access_token)

                        return response
                    return jsonify({"Erro":"Usuario nao consta em nossa base de dados."})

@auth_bp.post('/signup')
def signup():
    json = request.get_json()
    if not 'data' in json:
        return jsonify({"msg":"Insira uma chave 'data' e atribua um objeto json."})
    else: 
        if not type(json['data']) == type(json):
            return jsonify({"msg":"A chave data deve ser um objeto Json com as colunas do banco como chaves."})
        else:
            if json['data'] == {}:
                return jsonify({"msg":"As chaves devem ser as colunas do banco de dados."})
            else:
                data = json['data']
                with Session() as session:
                    colaborador = Colaborador(**data)
                    result = session.add(colaborador)
                    session.commit()

                    return jsonify({
                        "msg":"Usuário inserido com sucesso!",
                        "colab_inserted":True,
                        "new_colab_id": result
                    })

@auth_bp.post('/logout')
@jwt_required()
def logout():
    current_user = get_jwt_identity()
    unset_jwt_cookies(current_user)
    return current_user