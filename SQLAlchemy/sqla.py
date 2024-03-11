import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
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
    user = relationship("User", back_populates="address") # estabelece o relacionamento  
    def __repr__(self):
        return f'Address(id={self.id}, email={self.email_address})'
    
# Conexão com o banco de dados
engine = sqlA.create_engine('sqlite://')

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema do banco de dados
inspetor = sqlA.inspect(engine)

# Obtendo nome das tabelas
print(inspetor.get_table_names())
print(inspetor.default_schema_name)

# Estabelecer uma sessão (para que os dados persistam)
with Session(engine) as session:
    joao = User(
        name='joao victor',
        fullname='Joao Victor Carrijo',
        address=[Address(email_address='joaovictor@gmail.com')]
    )

    # Inserção de usuário com dois emails
    larissa = User(
        name='larissa',
        fullname='Larissa Carrijo',
        address=[Address(email_address='larissa@gmail.com'),
                 Address(email_address='larissa@outlook.com')]      
    )

    # Inserção de usuário sem email
    pedro = User(name='pedro',fullname='Pedro Alves')      

    # Enviar para o BD.
    session.add_all([joao, larissa, pedro])

    # Commitando os dados no banco.
    session.commit()