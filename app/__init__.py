from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

goodplace = Flask(__name__)
goodplace.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(goodplace)
migrate = Migrate(goodplace, db)

manager = Manager(goodplace)
manager.add_command('db', MigrateCommand)

from app.controllers import default
