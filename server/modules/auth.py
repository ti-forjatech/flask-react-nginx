from flask import Blueprint, jsonify, request
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from .connection import engine
from .models import Colaborador
from .cryptopass import generate_pass, decode_pass

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
Session = sessionmaker(bind=engine)

@auth_bp.post('/login')
def login():
    json = request.get_json()
    if not 'data' in json:
        return jsonify({"msg":"Insira uma chave 'data' e atribua um objeto json."})
    else:
        if not type(json['data']) == type(json):
            return jsonify({"msg":"A chave 'data' deve ser um objeto Json com as colunas do banco como chaves."})
        else:
            if json['data'] == {}:
                return jsonify({"msg":"As chaves de 'data' devem ser 'colab_login' e 'colab_senha'."})
            else:
                data = json['data']
                stmt = select(Colaborador).where(Colaborador.colab_login == data['colab_login'])
                print(stmt)
                with Session() as session:
                    for row in session.execute(stmt):
                        colab = row[0]
                        password_ok = decode_pass(data['colab_password'], colab.colab_senha)
                        if password_ok:
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
                            return jsonify(user_composition)
                        return jsonify({"Erro":"Nao autorizado!"})
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
            if json['data'] != {}:
                data = json['data']
                user_password = generate_pass(data['colab_senha'])

                colaborador = Colaborador(
                    colab_matricula=data['colab_matricula'],
                    colab_nome=data['colab_nome'],
                    colab_cpf=data['colab_cpf'],
                    colab_login=data['colab_login'],
                    colab_senha=user_password,
                    colab_status=data['colab_status']
                )

                with Session() as session:
                    result = session.add(colaborador)
                    session.commit()

                    return jsonify({
                    "colab_inserted":True,
                    "new_colab_id": result
                    })
            else:
                return jsonify({"msg":"As chaves devem ser as colunas do banco de dados."})

@auth_bp.post('/logout')
def logout():
    return jsonify({"msg": "LOGOUT"})