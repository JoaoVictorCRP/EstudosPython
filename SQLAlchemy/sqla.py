import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column

Base = declarative_base()
# As classes que se tornarão entidades devem herdar de declarative_base. 

class User(Base):
    __tablename__ = 'user_account'
    # Atributos
    id = Column(sqlA.Integer, primary_key=True, autoincrement=True)
    name = Column(sqlA.String)
    fullname = Column(sqlA.String)


class Address(Base):
    __tablename__ = 'user_address'
    # Atributos
    id = Column(sqlA.Integer, primary_key=True, autoincrement=True)
    email_addres = Column(sqlA.String(50), nullable=False) # NOT NULL
    user_id = Column(sqlA.Integer, sqlA.ForeignKey("user_account.id"))