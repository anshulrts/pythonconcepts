import math

class Circle:
    # Python doesn't have the concept of public, private accesses.
    # Python follows convention over restrictions.
    # For Non Public members, use _ before the name
    # However, this is just a convention, so if you try to access obj._name from outside the class,
    # you'll be able to access it. But it's bad practise, so avoid.
    _name = ""


    # Constructor
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)

circle_1 = Circle(42)
circle_2 = Circle(7)

print(circle_1)
print(circle_2)

print(circle_1.radius)
print(circle_1.calculate_area())

print(circle_2.radius)
print(circle_2.calculate_area())

# Can change its value from outside
circle_1.radius = 40
print(circle_1.radius)
print(circle_1.calculate_area())