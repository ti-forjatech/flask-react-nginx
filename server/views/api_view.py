from flask import Blueprint, Response, jsonify

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/test", methods=["GET"])
def index() -> Response:
    """Defines the main website view"""
    return jsonify("Testando o app, funfou!")

@api_bp.get("/data")
def get_data() -> Response:
    data = {
        "api_name":"forjatech api",
        "api_version":"0.4",
        "api_dev_start_date":"21/05/2023",
        "api_author":"Thyéz de Oliveira Monteiro",
        "api_description":"API geral do site forjaTech."
    }
    return jsonify(data)
