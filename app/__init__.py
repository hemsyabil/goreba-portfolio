from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'  

db = SQLAlchemy()

def create_app(config_class='app.config.DevelopmentConfig'):
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Add user loader after initializing login_manager
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User  # Import inside function to avoid circular imports
        return User.query.get(int(user_id))
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.portfolios import portfolio_bp
    # from app.routes.blog import blog_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(portfolio_bp)
    # app.register_blueprint(blog_bp)
    
    return app
