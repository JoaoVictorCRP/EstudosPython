from fastapi import FastAPI
from product import Product
from inDB import generate_products
from json_db import JsonDB

# Devemos instalar também a biblioteca Uvicorn para rodar no servidor local.
# Rode com: uvicorn <nome_arquivo>:<var_FastApi> --reload     (reload fará o recarregamento quando houver mudanças)

app = FastAPI()
productDB = JsonDB(path='./data/products.json')

@app.get('/products')
def get_products():
    return productDB.read()

@app.post('/products')
def create_product(product: Product):
    productDB.insert(product)
    return { "status": "inserted" }

# acesse /docs para um painel de testes das APIs
# acesse /redoc para visualizar as requisições ao vivo 