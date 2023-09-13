class Person:
    def __init__(self,name, age):
        self.name = str(name)
        self.age = int(age)



person_A= Person("Alice",25)
person_B= Person("Bob", 30)

print(f"{person_A.name} is {person_A.age} years old.")

print(f"{person_B.name} is {person_B.age} years old.")
