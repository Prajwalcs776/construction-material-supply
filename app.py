from flask import Flask
from config import Config
from models import db
from controllers.main_controller import main_bp
from controllers.db_controller import db_bp
from controllers.auth_controller import auth_bp
from controllers.dashboard_controller import dashboard_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(db_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
