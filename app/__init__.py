from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

goodplace = Flask(__name__)
goodplace.config.from_object('config')

db = SQLAlchemy(goodplace)  
migrate = Migrate(goodplace, db)

manager = Manager(goodplace)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(goodplace)

from app.models import tables
from app.controllers import default
