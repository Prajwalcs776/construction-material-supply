from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    session
)
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from models import db
from models.user_model import create_user, authenticate_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    role = request.form.get("role", "Contractor").strip()
    contractor_license_number = request.form.get(
        "contractor_license_number", ""
    ).strip()

    if not name:
        return jsonify({"error": "Name is required"}), 400
    if not email:
        return jsonify({"error": "Email is required"}), 400
    if not password:
        return jsonify({"error": "Password is required"}), 400
    if not role:
        return jsonify({"error": "Role is required"}), 400
    if role == "Contractor" and not contractor_license_number:
        return jsonify({
            "error": "Contractor license number is required"
        }), 400

    try:
        create_user(
            name=name,
            email=email,
            password=password,
            role=role,
            contractor_license_number=(
                contractor_license_number
                if role == "Contractor"
                else None
            )
        )
        return redirect(url_for("auth.login"), code=302)

    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "error": "Email already registered"
        }), 409

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({
            "error": "Database error"
        }), 503


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    if not password:
        return jsonify({"error": "Password is required"}), 400

    try:
        user = authenticate_user(email, password)

        if user is None:
            return jsonify({
                "error": "Invalid email or password"
            }), 401

        session["user_id"] = user.id
        session["user_name"] = user.name
        session["role"] = user.role
        session["contractor_license_number"] = (
            user.contractor_license_number
        )

        if user.role == "Supply Manager":
            return redirect(
                url_for("dashboard.manager_dashboard"),
                code=302
            )

        if user.role == "Contractor":
            return redirect(
                url_for("dashboard.contractor_dashboard"),
                code=302
            )

        return jsonify({
            "error": "Invalid user role"
        }), 403

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({
            "error": "Database error"
        }), 503


@auth_bp.route("/manager/admin-login", methods=["GET", "POST"])
def manager_admin_login():

    # Only an authenticated Supply Manager can access this page.
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "Supply Manager":
        return redirect(url_for("auth.login"))

    if request.method == "GET":
        return render_template("manager_admin_login.html")

    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    if not password:
        return jsonify({"error": "Password is required"}), 400

    try:
        user = authenticate_user(email, password)

        if user is None or user.role != "Supply Manager":
            return jsonify({
                "error": "Invalid manager credentials"
            }), 401

        session["manager_admin_verified"] = True

        return redirect(
            url_for("dashboard.manager_dashboard"),
            code=302
        )

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({
            "error": "Database error"
        }), 503


@auth_bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
