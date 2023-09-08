# Inner functions, also known as nested functions, are functions that you define inside other functions.
# In Python, this kind of function has direct access to variables and names defined in the enclosing
# function. Inner functions have many uses, most notably as closure factories and decorator functions.
# Eg

def outer_func():
    def inner_func():
        print("Hello World") # Hello World
    inner_func()

outer_func()

# The core feature of inner functions is their ability to access variables and objects from their
# enclosing function even after this function has returned. The enclosing function provides a
# namespace that is accessible to the inner function:

def out_func(who):
    def inn_func():
        print(f"Hello, {who}") # Hello, NY
    inn_func()

out_func("NY")
