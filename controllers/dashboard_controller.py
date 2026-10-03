from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/manager/dashboard", methods=["GET"])
def manager_dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "Supply Manager":
        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        dashboard_type="manager"
    )


@dashboard_bp.route("/contractor/dashboard", methods=["GET"])
def contractor_dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "Contractor":
        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        dashboard_type="contractor"
    )


@dashboard_bp.route("/manager/materials", methods=["GET"])
def manager_materials():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "Supply Manager":
        return redirect(url_for("auth.login"))

    return render_template("materials.html")
