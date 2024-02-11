from flask import Flask
from flask_login import LoginManager
from .models import User, db




def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///taskflowpro.db"
    app.config["SECRET_KEY"] = "SECRET KEY"

    db.init_app(app)
    


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")


    with app.app_context():
        db.create_all()



    login_manager = LoginManager()
    login_manager.login_view = "auth.login_page"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        try:
            if id is not None:
                user = User.query.get(int(id))
                if user:
                    return user
        except Exception as e:
            print(f"Error loading user: {e}")
        return None
    return app