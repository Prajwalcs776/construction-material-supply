from flask import Blueprint, redirect, url_for


main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def home():
    return redirect(url_for("auth.login"))
