from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sqla
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Date, Column, Boolean

# --- Definindo Objetos em Flask ---
# No desenvolvimento de aplicativos, um "model" refere-se a representação real (ou conceitual) de algum objeto.
# Por exemplo, caso esteja fazendo um app para uma concessionária, você talvez defina um model chamado "car" que
# encapsule todos os atributos e comportamentos de um carro.

# Suponhamos que você esteja desenvolvendo uma To-Do List com Tasks, e cada Task pertence a um usuário.
# Antes de você pensar mais a fundo sobre o relacionamento destas entidades, comece definindo os objetos para
# Task e Users.


# --- Banco de Dados + Flask ---
# O pacote flask-sqlalchemy aproveita o SQLalchemy para configurar e informar a estrutura do banco de dados.
# Você irá definir um modelo que irá ser passado ao banco de dados herdando do objeto db.Model, Apartir disto,
# definimos o atributo desses models como instâncias db.Column. Para cada coluna, você deve especificar
# um tipo de dado, e então passar esse data type para o comando db.Column como primeiro argumento.


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
Base = declarative_base()
db = sqla(model_class=Base)
db.init_app(app)


# --- A DEFINIÇÃO ---
# Pelo fato da definição do model ocupar um espaço conceitual diferente da configuração do aplicativo, faça com
# que o models.py mantenha definições de model de forma separada do app.py. O modelo do task deve ser construído
# para que tenha os atributos da seguinte maneira

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Valor de identificação única
    name = db.Column(db.String(100), nullable=False) # O nome ou o título da task settada pelo usuário
    note = db.Column(db.String(100)) # Descrição ou comentários adicionais
    creation_date = db.Column(db.Date()) # Data e o horário que a task foi criada
    due_date = db.Column(db.Date()) # Data e o horário que a task deve ser concluída, se houver.
    completed = db.Column(db.Boolean()) # Indica se a task foi concluída ou não
