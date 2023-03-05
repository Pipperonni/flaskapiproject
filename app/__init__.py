from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
login.init_app(app)
cors.init_app(app)

login.login_view = '/sign_in'
login.login_message = 'Make sure you login'

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)

from app.blueprints.collect import bp as collect_bp
app.register_blueprint(collect_bp)

from app.blueprints.api import bp as api_bp
app.register_blueprint(api_bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    cors.init_app(app)

    login.login_view = '/sign_in'
    login.login_message = 'Make sure you login'

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.collect import bp as collect_bp
    app.register_blueprint(collect_bp)

    from app.blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
