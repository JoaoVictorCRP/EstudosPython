from product import Product

def generate_products():
    list_products = []

    for i in range(10):
        p = Product(name=f'Produto {i+1}', price= 1.99*i)
        list_products.append(p)

    return list_products