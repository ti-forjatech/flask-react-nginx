from flask import Blueprint
from .estoque_categorias import categorias_bp
from .estoque_itens import itens_bp

estoque_bp = Blueprint("estoque", __name__, url_prefix="/estoque")

# registro das Blueprints de Categorias e Itens
estoque_bp.register_blueprint(categorias_bp)
estoque_bp.register_blueprint(itens_bp)