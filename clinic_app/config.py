import os

class Config:
    # Строка подключения к MySQL в Docker Compose
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://user:password@db/medcopreg"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "da4ba06f7e16bb5294eb76d6555d6a3df767f5e2a018bb6a264d4a23d6ffffe1"
