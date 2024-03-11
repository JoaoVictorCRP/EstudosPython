import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column

Base = declarative_base()
# As classes que se tornarão entidades devem herdar de declarative_base. 

class User(Base):
    __tablename__ = 'user_account'
    # Atributos
    id = Column(sqlA.Integer, primary_key=True, autoincrement=True)
    name = Column(sqlA.String)
    fullname = Column(sqlA.String)
    address = relationship("Address", back_populates="user", cascade="all, delete-orphan") # CASCATA: se uma das tabelas for deletada, a tabela órfã será deletada automaticamente.
    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, fullname={self.fullname})'

class Address(Base):
    __tablename__ = 'user_address'
    # Atributos
    id = Column(sqlA.Integer, primary_key=True, autoincrement=True)
    email_address = Column(sqlA.String(50), nullable=False) # (NOT NULL)
    user_id = Column(sqlA.Integer, sqlA.ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="address", cascade="all, delete-orphan") # estabelece o relacionamento  
    def __repr__(self):
        return f'Address(id={self.id}, email={self.email_address})'