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

print(circle_1) # <__main__.Circle object at 0x000001CEE0A2EFD0>
print(circle_2) # <__main__.Circle object at 0x000001CEE0A2EF70>

print(circle_1.radius) # 42
print(circle_1.calculate_area()) # 5541.77

print(circle_2.radius) # 7
print(circle_2.calculate_area()) # 153.94

# Can change its value from outside
circle_1.radius = 40
print(circle_1.radius) # 40
print(circle_1.calculate_area()) # 5026.55