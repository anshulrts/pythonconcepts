# Functions in Python start with def keyword
# The return value of a Python function can be any object.
# Everything in python is an object. So your functions can return numeric, collections, user
# defined objects, classes, functions even modules & packages.
# They always return a value, even if you don't specify a return statement

# You can omit the return value of a function and use a bare return without a return value.
# You can also omit the entire return statement. In both cases, the return value will be None.

# Returning Multiple Values
# In Python, you can return multiple values. You just need to separate them by comma.

def returnmultiple():
    return 1, 2, 3

desc = returnmultiple()
print(desc) # (1, 2, 3)
# desc becomes a tuple here storing all 3 values

a, b, c = returnmultiple()
print(a,b,c) # 1 2 3
# This concept of unpacking in 3 variables is called a iterable unpacking.