from product import Product
import json

def generate_products():
    file = open('./data/products.json')
    data =  json.loads((file.read())) # load-s (load string) => https://stackoverflow.com/questions/39719689/what-is-the-difference-between-json-load-and-json-loads-functions
    file.close()
    return data