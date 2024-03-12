import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import func

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
print(f'Nome das tabelas: {inspetor.get_table_names()}')
print(f'Nome do esquema: {inspetor.default_schema_name}')

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

# Realizando consulta na entidade usuário
stmt = sqlA.select(User).where(User.name.in_(['joao victor', 'larissa']))
print('\n--- Recuperando usuários a partir de condição de filtragem ---')
for user in session.scalars(stmt):
    print(user)

# Realizando consulta na entidade endereço
stmt_address = sqlA.select(Address).where(Address.user_id.in_([2])) # usuário de id 2
print("\n--- Recuperando os endereços de email de Larissa ---")
for address in session.scalars(stmt_address):
    print(address)

# ORDER BY
print('\n--- Recuperando de maneira ordenada ---')
order_stmt = sqlA.select(User).order_by(User.fullname)
for result in session.scalars(order_stmt):
    print(result)

# JOIN
print('\n--- Juntando Dados das entidades ---')
join_stmt = sqlA.select(User.fullname, Address.email_address).join_from(Address, User) # A cláusula de junção é detectada automaticamente de acordo com a FK.
# print(join_stmt) # Query realizada
for result in session.scalars(join_stmt):
    print(result)


# Estabelecendo uma coneção com o banco de dados. (Ao invés de uma sessão)
connection = engine.connect()
results = connection.execute(join_stmt).fetchall()
print('\n--- Executando o JOIN a partir de uma conexão ---')
for result in results:
    print(result) # Diferentemente do retorno do statement de sessão, este retornará tanto o fullname quanto o endereço de email.


# COUNT
print('\n--- Total de instâncias em User ---')
stmt_count = sqlA.select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
    print(result)