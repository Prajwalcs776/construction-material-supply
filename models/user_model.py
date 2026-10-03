from models import db
from sqlalchemy import text


def create_user(name, email, password, role, contractor_license_number=None):
    query = text("""
        INSERT INTO users
        (name, email, password, role, contractor_license_number)
        VALUES
        (:name, :email, :password, :role, :contractor_license_number)
    """)

    result = db.session.execute(
        query,
        {
            "name": name,
            "email": email,
            "password": password,
            "role": role,
            "contractor_license_number": contractor_license_number
        }
    )

    db.session.commit()

    return result.lastrowid


def authenticate_user(email, password):
    query = text("""
        SELECT
            id,
            name,
            email,
            password,
            role,
            contractor_license_number
        FROM users
        WHERE email = :email
        AND password = :password
        LIMIT 1
    """)

    result = db.session.execute(
        query,
        {
            "email": email,
            "password": password
        }
    )

    return result.fetchone()
