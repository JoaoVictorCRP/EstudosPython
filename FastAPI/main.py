# Devemos instalar também a biblioteca Uvicorn para rodar no servidor local.
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_language():
    return {"Hello": "World"}
    # Retorna chave e valor