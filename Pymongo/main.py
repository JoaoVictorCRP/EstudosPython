import pymongo as pm
import os
from dotenv import load_dotenv
from datetime import datetime

# Atribuindo Connection String
load_dotenv()
passwd = os.getenv('MONGO_PASSWORD')
connection = f'mongodb+srv://joaovictorxl120:{passwd}@cluster0.3rqdk7b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
# Conectando cliente
client = pm.MongoClient(connection)
# Selecionando BD
db = client.TesteBD
# Listando coleções
# print(db.list_collections)
# Selecionando Coleção
collection = db.pessoas
# Criando um documento
post = {
    "nome":"Mike",
    "idade":23,
    "descrição":"Programador fullstack Python, especialista em Django.",
    "tags":["python","programador","django","jovem"],
    "date": datetime.now()
}
# Preparando para submeter as infos 
post_id = collection.insert_one(post).inserted_id
print(post_id)
