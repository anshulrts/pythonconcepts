# This module is just for demonstration purpose. You should try
# to avoid using global variables
a = 10
city = "Hamburg"

def func():
    # Following 2 statements will result in UnBoundLocal Error
    # This is because we cannot have a variable both as local and global
    # So python decides that we want to have a local variable and throws error
    # in first statement
    #
    # print(a)
    # a = 20
    # print(a)

    # Cannot do this.
    # You can only access a global variable directly but in order to modify,
    # you need to declare 'a' as a global variable using global keyword
    # a = a * 10
    
    global a
    a = 20
    print(a)

def same_name():
    # If you declare a local var with same name as global, local will
    # take precedence
    a = 33
    print(a)

def non_local():
    x = "local"

    def inner():
        # If you declare a variable with nonlocal keyword, changes will reflect
        nonlocal x
        x = "Changed Inside"
        print(x)
    
    inner()
    print(x)

def global_nested_func():
    city = "Sydney"

    def inside():
        global city
        city = "Mumbai"

    print("City inside local function before calling inside() : ", city)
    inside()
    print("City inside local function after calling inside() : ", city)

def start():
    func()
    # This will print 20 as global a has been changed in func()
    print(a)
    same_name()
    non_local()
    print(city)
    global_nested_func()
    print("City inside global space before calling global_nested_func() : ", city)