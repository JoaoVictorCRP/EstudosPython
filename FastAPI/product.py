from pydantic import BaseModel
# Veja como o pydantic é uma biblioteca que lida de maneira bem mais fácil com objetos.

# Jeito tradicional:
class Product:
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price
        # COISA FEIA...

# Jeitinho BaseModel:
class Product(BaseModel):
    name:str
    price:float
    # QUE LINDO, QUE LINDO!