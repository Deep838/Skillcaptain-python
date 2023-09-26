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











import unittest


class TestProduct(unittest.TestCase):

    def test_product_attributes(self):
        biscuit = Product("Biscuit", 40, 3)
        self.assertEqual(biscuit.name, "Biscuit")
        self.assertEqual(biscuit.price, 40)
        self.assertEqual(biscuit.quantity, 3)


class TestCart(unittest.TestCase):

    def setUp(self):
        self.biscuit = Product("Biscuit", 40, 3)
        self.chocolate = Product("Chocolate", 80, 5)
        self.coffee = Product("Coffee", 30, 2)
        self.my_cart = Cart("Deep")

    def test_add_to_cart(self):
        self.my_cart.add_to_cart(self.biscuit)
        self.assertEqual(len(self.my_cart.product_list), 1)
        self.assertEqual(self.my_cart.product_list[0], self.biscuit)

    def test_remove_from_cart(self):
        self.my_cart.add_to_cart(self.biscuit)
        self.my_cart.add_to_cart(self.chocolate)
        self.my_cart.remove_from_cart(self.biscuit)
        self.assertEqual(len(self.my_cart.product_list), 1)
        self.assertEqual(self.my_cart.product_list[0], self.chocolate)

    def test_display_cart(self):
        import io
        from unittest.mock import patch

        self.my_cart.add_to_cart(self.biscuit)
        self.my_cart.add_to_cart(self.chocolate)

        # Redirect stdout to capture print output
        with io.StringIO() as buffer, patch("sys.stdout", buffer):
            self.my_cart.display_cart()
            output = buffer.getvalue()

        expected_output = "Biscuit - Price:  40.00/- - Quantity: 3\nChocolate - Price:  80.00/- - Quantity: 5\n"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
