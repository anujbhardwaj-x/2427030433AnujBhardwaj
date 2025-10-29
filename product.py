class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

class Clothing(Product):
    def __init__(self, name, price, size, fabric):
        super().__init__(name, price)
        self.size = size
        self.fabric = fabric

a = Electronics("Phone", 20000, "Apple", "2 years")
b = Clothing("T-shirt", 2000, "L", "Cotton")

print(a.name, a.price, a.brand, a.warranty)
print(b.name, b.price, b.size, b.fabric)
