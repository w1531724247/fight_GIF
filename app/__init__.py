from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from api import square as square_blueprint
    app.register_blueprint(square_blueprint, url_prefix='/square')
    from api import category as category_blueprint
    app.register_blueprint(category_blueprint, url_prefix='/category')
    from tools import tools as tools_blueprint
    app.register_blueprint(tools_blueprint, url_prefix='/tools')

    return app