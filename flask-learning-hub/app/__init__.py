import os
from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    
    # Configuration setup for local SQLite database
    app.config['SECRET_KEY'] = 'flask-learning-hub-secret-key-1804'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'flask_hub.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ensure the instance folder exists for SQLite to create its file
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the database extension with the app
    db.init_app(app)

    # Register blueprints (We will configure views inside these shortly)
    from .hub.views import hub_bp
    from .api.views import api_bp

    app.register_blueprint(hub_bp, url_prefix='')
    app.register_blueprint(api_bp, url_prefix='/api')

    # Automatically build database tables if they do not exist
    with app.app_context():
        db.create_all()

    return app