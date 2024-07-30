class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code


name, code = tuple(input().split())
p1 = Product("codetree", "50")
p2 = Product(name, code)

print(f'product {p1.code} is {p1.name}')
print(f'product {p2.code} is {p2.name}')