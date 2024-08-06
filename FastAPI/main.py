from fastapi import FastAPI
from inDB import generate_products

# Devemos instalar também a biblioteca Uvicorn para rodar no servidor local.
# Rode com: uvicorn <nome_arquivo>:<var_FastApi> --reload     (reload fará o recarregamento quando houver mudanças)

app = FastAPI()

products = generate_products()

@app.get('/products')
def get_products():
    return products
