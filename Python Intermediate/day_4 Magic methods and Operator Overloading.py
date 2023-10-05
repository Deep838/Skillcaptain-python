class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

# Creating Point objects
point1 = Point(2, 3)
point2 = Point(2, 3)
point3 = Point(4, 5)

# Using the == operator to compare Point objects
print(point1 == point2)  # True, as the coordinates are the same
print(point1 == point3)  # False, as the coordinates are different
