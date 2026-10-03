from models import db
from sqlalchemy import text


def create_material(material_name, category, quantity, status):
    query = text("""
        INSERT INTO materials
        (material_name, category, quantity, status)
        VALUES
        (:material_name, :category, :quantity, :status)
    """)

    result = db.session.execute(
        query,
        {
            "material_name": material_name,
            "category": category,
            "quantity": quantity,
            "status": status
        }
    )

    db.session.commit()
    return result.lastrowid


def get_all_materials():
    query = text("""
        SELECT
            id,
            material_name,
            category,
            quantity,
            status
        FROM materials
        ORDER BY id DESC
    """)

    result = db.session.execute(query)
    return result.fetchall()
