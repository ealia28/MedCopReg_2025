from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')  # Загружаем конфиг
    
    db.init_app(app)

    # Импортируем модели, чтобы SQLAlchemy знал про них
    from app import models  

    # Подключаем маршруты
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
