import os


from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import  LoginManager
from flask_openid import OpenID
from config import BASE_DIR


app = Flask(__name__)
app.config.from_object(Config)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(BASE_DIR, "tmp"))
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import view
from app import model
