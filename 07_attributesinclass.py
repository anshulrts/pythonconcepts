# There are 2 types of attributes in Python
# 1. Class attributes - which we define in class body directly.
# Class attributes belong to their containing class.
# Their data is common to the class and all its instances.
# 2. Instance attributes - An instance is a variable that you define inside a method.
# Instance attributes belong to a concrete instance of a given class.
# Their data is only available to that instance and defines its state.

# Class Attribute
class ObjectCounter:
    # defining a class attribute
    num_instances = 0

    def __init__(self):
        type(self).num_instances += 1

ObjectCounter()
ObjectCounter()
ObjectCounter()
ObjectCounter()

print(ObjectCounter.num_instances)

counter = ObjectCounter()
# We can access class attribute using either class name(above) or object
print(counter.num_instances)

# However, if you need to modify a class attribute, then you must use the class itself
# rather than one of its instances.



# Instance Attributes
# Python lets you dynamically attach attributes to existing objects that you’ve already created.
# However, you most often define instance attributes inside instance methods,
# which are those methods that receive self as their first argument.
# Note: Even though you can define instance attributes inside any instance method,
# it’s best to define all of them in the .__init__() method, which is the instance initializer.
# This ensures that all of the attributes have the correct values when you create a new instance.
# Additionally, it makes the code more organized and easier to debug.

class Car:
    def __init__(self, make, model, year, color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color
# Note: Inside a class, you must access all instance attributes through the self argument.
# This argument holds a reference to the current instance, which is where the attributes belong and live.
