with open("cars.txt", "r") as file:
    car_types = iter(file)


    try:
        # Use next() to iterate through each line
        while True:
            line = next(car_types)
            # Process the line
            print(line)

    except StopIteration:
        pass