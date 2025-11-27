# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate 

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.Config')
    
#     db.init_app(app)
#     migrate.init_app(app, db)
    
#     from app import models

#     with app.app_context():
#         # Это создаст все таблисы автоматически
#         db.create_all()
#         print("✅ Database tables created successfully")

#     from app.routes import main_bp
#     app.register_blueprint(main_bp)

#     return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app import models

    with app.app_context():
        # Искусственная уязвимость: использование eval() с небезопасным вводом
        user_input = "2+2"
        eval(user_input)  # Bandit должен отметить это как HIGH risk

        # Секрет: тестовый ключ для проверки Gitleaks
        SECRET_KEY = "TEST_SECRET_KEY_12345"

        # Создание таблиц
        db.create_all()
        print("✅ Database tables created successfully")

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    # Искусственная ошибка для Pylint (например, неиспользуемая переменная и нарушение стиля)
    unused_var = 42

    return app
