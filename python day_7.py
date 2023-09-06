
num=int(input("add a integer: "))

def is_even():
    if num % 2 == 0:
        return (f"{num} is even.")
    else:
        return (f"{num} is odd.")

print(is_even())