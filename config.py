import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY", 'you-will-never-guess')
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "app.db"))
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False