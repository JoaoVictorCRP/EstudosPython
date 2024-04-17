import pymongo as pm
import os
from dotenv import load_dotenv
from datetime import datetime
from pprint import pprint # Pretty print de dados

# Atribuindo Connection String
load_dotenv()
passwd = os.getenv('MONGO_PASSWORD')
connection = f'mongodb+srv://joaovictorxl120:{passwd}@cluster0.3rqdk7b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Conectando cliente
client = pm.MongoClient(connection)

# Selecionando BD
db = client.TesteBD

# Listando coleções
print(db.list_collection_names())

# Selecionando Coleção
collection = db.pessoas

# Criando um documento
# post = {
#     "nome":"Mike",
#     "idade":23,
#     "descrição":"Programador fullstack Python, especialista em Django.",
#     "tags":["python","programador","django","jovem"],
#     "date": datetime.now()
# }

# Submetendo as infos 
# post_id = collection.insert_one(post).inserted_id

# Fazendo uma query
# pprint(collection.find_one())

# Bulk inserts
bulk_post = [{
        "nome":"Anne",
        "idade": 19,
        "titulo":"Olá, sou a Anne!",
        "descrição":"Analista de dados, Expert em PowerBI",
        "tags":["dados","estatística","PowerBI","DBA"],
        "date": datetime.now()
    },
    {
        "nome":"Leonardo",
        "sobrenome":"Dias dos Anjos",               # Veja que os documentos possuem atributos diferentes!
        "idade":27,                                 # em um BD noSQL, nossos inserts simplesmente não possuem
        "descrição":"Gestor de TI",                 # uma estrutura fixa.
        "tags":["redes","infraestrutura","suporte","técnico"],
        "date": datetime.now()
    },
    {
        "nome":"João Pedro",
        "idade": 16,
        "titulo":"Aprendiz de Programação",
        "descrição":"Aspirante a desenvolvedor, Futuro gênio",
        "tags":["menor","básico","jovem","talento", "scratch", "portugol"],
        "date": datetime.now()
    },
]
bulk_insert = collection.insert_many(bulk_post)

# Recuperação final
cursor = collection.find({})
for d in cursor:
    pprint(d)