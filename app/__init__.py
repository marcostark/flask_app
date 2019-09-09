from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Manager
from flask_migrate import Migrate, MigrateCommand


# Variavel que tem todo o controle da aplicacao
app = Flask(__name__)
app.config.from_object('config') #Passando configurações
db = SQLAlchemy(app)

# Migrações
migrate = Migrate(app, db)

# Controle de informações que será passado na execução
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import tables, forms
from app.controllers import default

