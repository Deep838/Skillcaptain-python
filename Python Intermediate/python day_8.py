#1. Create a Product class

class Product:

    #2 & 3 class attributes and parameteres
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)

#4. product's info
    def product_info(self):
        print(f"product {self.name}'s price is {self.price} and quantity {self.quantity}")

#5. collect Product info and create a new product object
    def register_product(products):
        print("Product Registration")
        while True:
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            quantity = input("Enter quantity: ")

            new_product = Product(name, price, quantity)
            products.append(new_product)
            print("Product registered successfully!")
            break

#7. storing the products info in a list
products = []
while True:
    Product.register_product(products)
    another = input("Do you want to register another Product? (yes/no): ")
    if another.lower() != "yes":
        break

print("\nRegistered Products:")
for idx, product in enumerate(products, start=1):
    print(f"Product: {idx}")
    print(f"Name: {product.name}")
    print(f"Price: {product.price}")
    print(f"quantity: {product.quantity}")
