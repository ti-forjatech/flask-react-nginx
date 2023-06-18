from flask import Blueprint, Response, jsonify
from .colaboradores import colaboradores_bp
from .cargos import cargos_bp
from .enderecos import enderecos_bp
from .bases import bases_bp
from .fornecedores import fornecedores_bp
from .notas import notas_bp
from .cotacoes import cotacoes_bp
from .estoque import estoque_bp
from .centros_custo import centros_custo_bp
from .sub_centros_custo import sub_centros_custo_bp
from .clientes import clientes_bp
from .tipos_documento import tipos_documento_bp
from .cargo_acessos import cargo_acessos_bp
from ..modules.auth import auth_bp

# criação das Blueprints da API: app e v2
app_bp = Blueprint("app", __name__, url_prefix="/app")
v2_bp = Blueprint("v2", __name__, url_prefix="/v2")

# Registro do v2 no app
app_bp.register_blueprint(v2_bp)
# Registro do auth no app
app_bp.register_blueprint(auth_bp)

# Registro de todas Blueprints da API V2
v2_bp.register_blueprint(colaboradores_bp)
v2_bp.register_blueprint(cargos_bp)
v2_bp.register_blueprint(bases_bp)
v2_bp.register_blueprint(enderecos_bp)
v2_bp.register_blueprint(fornecedores_bp)
v2_bp.register_blueprint(notas_bp)
v2_bp.register_blueprint(cotacoes_bp)
v2_bp.register_blueprint(estoque_bp)
v2_bp.register_blueprint(centros_custo_bp)
v2_bp.register_blueprint(sub_centros_custo_bp)
v2_bp.register_blueprint(tipos_documento_bp)
v2_bp.register_blueprint(cargo_acessos_bp)
v2_bp.register_blueprint(clientes_bp)

@app_bp.get("/data")
def get_data() -> Response:
    data = {
        "api_name":"Rio Services core API",
        "api_version":"2.5.0",
        "api_dev_start_date":"09/07/2023",
        "api_author":"Forjatech Soluções Tecnológicas (Thyéz de Oliveira Monteiro)",
        "api_author_email":"thyezoliveira.homeoffice@gmail.com",
        "api_description":"API central da Rio Services. Esta API provê recursos computacionais de alta performance e escalabilidade para operaçoes de recolhimento, armazenamento e proteção adequados dos dados sensiveis da empresa."
    }
    return jsonify(data)