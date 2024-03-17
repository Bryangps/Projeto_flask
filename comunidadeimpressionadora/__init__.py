from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

#app é uma instacia da classe Flask
app = Flask(__name__) #coloca o site no ar


app.config['SECRET_KEY'] = 'ecb55781950cc9a088f296affd8e7b47'
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db' #informa onde vai ficar o banco de dados do meu aplicativo

database = SQLAlchemy(app) #cria a instancia do banco de dados
#vai criar um banco de dados usando essa classe SQLALchmey de acordo com as configurações do nosso app.
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table('usuario'):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print('Base de Dados criado')
else:
    print('Base de dados já existente')

from comunidadeimpressionadora import routes
