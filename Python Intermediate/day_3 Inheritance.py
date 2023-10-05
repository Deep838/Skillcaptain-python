class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"This vehicle is {self.brand}, {self.model}")


class Truck(Vehicle):
    def __init__(self,brand, model, load_capacity):
        self.load_capacity = load_capacity
        super().__init__(brand, model)

    def display_info(self):
        super().display_info()
        print(f"load capacity {self.load_capacity}")


truck = Truck("TATA","Prima 5530.S","40000 Kgs")

truck.display_info()