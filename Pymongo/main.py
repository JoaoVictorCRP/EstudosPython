import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Atribuindo Connection String
load_dotenv()
passwd = os.getenv('MONGO_PASSWORD')
connection = f'mongodb+srv://joaovictorxl120:{passwd}@cluster0.3rqdk7b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'


client = MongoClient(connection)
db = client.Projeto_Agenda
collection = db.contatos
print(collection.find_one({'nome':'Sarah'}))