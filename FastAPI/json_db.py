from pydantic import BaseModel
from product import Product
import json

class JsonDB(BaseModel):
    path:str

    def read(self):
        f = open(self.path)
        data = json.loads(f.read())
        f.close()
        return data
    
    def insert(self, product: Product):
        data = self.read()
        data['products'].append(product.model_dump()) #com o método model_dump, transformaremos o produto passado como parametro em um dicionário
        f = open(self.path, 'w')
        f.write(json.dumps(data)) #atualizando registros
        f.close()