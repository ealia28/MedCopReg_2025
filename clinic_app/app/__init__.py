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
import subprocess  # Добавили для создания уязвимости High
import sys

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app import models

    with app.app_context():
        # --- Bandit HIGH Risk ---
        # B602: subprocess_popen_with_shell_equals_true
        # Это гарантированный HIGH severity.
        subprocess.call("echo 'hacked'", shell=True)

        # --- Gitleaks ---
        # Лучше использовать формат, похожий на реальный токен, чтобы детектор сработал наверняка.
        # Например, фейковый AWS ключ:
        AWS_KEY = "AKIAIMNOJVGFDEXAMPLE" 

        # Создание таблиц
        db.create_all()
        print("✅ Database tables created successfully")

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    # --- Pylint ERROR (Blocker) ---
    # Это вызовет ошибку E1101 (no-member), так как у модуля sys нет атрибута 'this_does_not_exist'.
    # Это категория Error, а не Warning.
    print(sys.this_does_not_exist)

    return app
