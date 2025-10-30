from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')  # Загружаем конфиг
    
    db.init_app(app)
    migrate.init_app(app, db)
    # Импортируем модели, чтобы SQLAlchemy знал про них
    from app import models  

    # Подключаем маршруты
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
