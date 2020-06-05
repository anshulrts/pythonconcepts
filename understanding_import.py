# This is how we import a module in python
# import X imports the module X, and creates a reference to that module in the current namespace.
# Or in other words, after you’ve run this statement, you can use X.name to refer to things
# defined in module X.
import module1

# from X import * imports the module X, and creates references in the current namespace
# to all public objects defined by that module (that is, everything that doesn’t have a
# name starting with “_”). Or in other words, after you’ve run this statement, you can
# simply use a plain name to refer to things defined in module X. But X itself is not
# defined, so X.name doesn’t work. And if name was already defined, it is replaced by the
# new version. And if name in X is changed to point to some other object, your module won’t
# notice.
# This is usually not recommended as you might fill the local symbol table en masse
from module2 import *

# from X import a, b, c imports the module X, and creates references in the current
# namespace to the given objects. Or in other words, you can now use a and b and c
# in your program.
from module3 import a1, b1

# Suppose there are two module having same name variables.
# Then the current module will take the value of the module defined later
from module4 import *
from module5 import *

def start():

    print(module1.x)
    print(module1._y)


    print(a)
    # _b is not accessible here as it is private to module2
    # as it is preceeded by _. NameError will occur here
    #print(_b)


    print(a1)
    print(b1)


    print(testvalue)