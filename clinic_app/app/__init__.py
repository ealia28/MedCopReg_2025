from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()

def create_app(testing=False):
    app = Flask(__name__)
    app.config.from_object('config.Config')

    if testing:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("✅ Database tables created successfully")
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate 
# import os
# import subprocess  # Добавили для создания уязвимости High
# import sys

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('config.Config')
    
#     db.init_app(app)
#     migrate.init_app(app, db)
    
#     from app import models

#     with app.app_context():
#         # --- Bandit HIGH Risk (Гарантированный) ---
#         # Мы имитируем получение данных извне (например, от пользователя)
#         unsafe_input = "some_user_input"
        
#         # Использование переменной внутри shell=True триггерит HIGH severity (B602)
#         subprocess.call("echo " + unsafe_input, shell=True)

#         # --- Альтернатива (Тоже HIGH) ---
#         # Использование yaml.load без SafeLoader (B506)
#         import yaml
#         yaml.load("!!python/object/apply:os.system ['rm -rf /']", Loader=yaml.Loader)

#         # --- Gitleaks ---
#         # Лучше использовать формат, похожий на реальный токен, чтобы детектор сработал наверняка.
#         # Например, фейковый AWS ключ:
#         AWS_KEY = "AKIAIMNOJVGFDEXAMPLE" 

#         # Создание таблиц
#         db.create_all()
#         print("✅ Database tables created successfully")

#     from app.routes import main_bp
#     app.register_blueprint(main_bp)

#     # --- Pylint ERROR (Blocker) ---
#     # Это вызовет ошибку E1101 (no-member), так как у модуля sys нет атрибута 'this_does_not_exist'.
#     # Это категория Error, а не Warning.
#     print(sys.this_does_not_exist)

#     return app







