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
# collection.insert_one(post).inserted_id

# Fazendo uma query
# pprint(collection.find_one())

# Bulk inserts
bulk_post = [{
        "nome":"Lindsey",
        "idade": 21,
        "titulo":"Oiee, sou a Lindsey",
        "descrição":"Analista de dados, Expert em PowerBI",
        "tags":["dados","estatística","PowerBI","DBA"],
        "date": datetime.now()
    },
    {
        "nome":"Leandro",
        "sobrenome":"Malandro",               # Veja que os documentos possuem atributos diferentes!
        "idade":55,                                 # em um BD noSQL, nossos inserts simplesmente não possuem
        "descrição":"Gestor de TI",                 # uma estrutura fixa.
        "tags":["redes","infraestrutura","suporte","técnico"],
        "date": datetime.now()
    },
    {
        "nome":"Enzo",
        "idade": 14,
        "titulo":"Aprendiz de Programação",
        "descrição":"Aspirante a desenvolvedor, Futuro gênio",
        "tags":["menor","básico","jovem","talento", "scratch", "portugol"],
        "date": datetime.now()
    },
]
collection.insert_many(bulk_post)

# Recuperando vários documentos:
# for document in collection.find():
#     pprint(document)

# Inserindo documento errado
# wrong_post = {
#     "nome":"Neguinho da Beija-Flor",
#     "idade": "?",
#     "titulo": "Olha o Beija-Flor aí, gente!",
#     "tags": ['carnaval','sapucaí','samba'],
#     "date": datetime(1976,2,10)
# }
# collection.insert_one(wrong_post)
# # Visualizando
# pprint(collection.find_one({"nome":"Neguinho da Beija-Flor"}))

# Deletando UM documento indesejado
# collection.delete_one({'nome':'Neguinho da Beija-Flor'})

# Deletando VÁRIOS documentos indesejados (Supondo que inserimos diversas vezes o Neguinho da Beija-Flor)
# for document in collection.find():
#     pprint(document)

# Contando documentos
cont_dados = collection.count_documents({'tags':'infraestrutura'})
print(cont_dados)