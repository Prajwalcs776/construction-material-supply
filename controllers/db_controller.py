from flask import Blueprint, jsonify
from models.db_helpers import execute_query

db_bp = Blueprint("db", __name__)


@db_bp.route("/test-db", methods=["GET"])
def test_db():
    try:
        execute_query("SELECT 1")
        return jsonify({
            "status": "success",
            "message": "Database connection successful"
        }), 200
    except Exception as exc:
        return jsonify({
            "status": "error",
            "message": "Database connection failed",
            "error": str(exc)
        }), 500
