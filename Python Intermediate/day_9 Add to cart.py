class Product:

    #2 & 3 class attributes and parameteres
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:

    def __init__(self, user_name):
        self.user_name = user_name
        self.product_list = []

    def add_to_cart(self, product):
        self.product_list.append(product)

    def remove_from_cart(self, product):
        self.product_list.remove(product)

    def display_cart(self):
        for item in self.product_list:
            print(f"{item.name} - Price: {item.price: .2f}/- - Quantity: {item.quantity}")



# Create some Product instances
biscuit = Product("Biscuit", 40, 3)
chocolate = Product("Chocolate", 80, 5)
coffee = Product("Coffee", 30, 2)

# Create a Cart and add products to it
my_cart = Cart("Deep")
my_cart.add_to_cart(biscuit)
my_cart.add_to_cart(chocolate)
my_cart.add_to_cart(coffee)

# Display the contents of the cart
my_cart.display_cart()