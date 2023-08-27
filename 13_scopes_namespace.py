# Namespace
# An assignment statement creates a symbolic name that you can use to reference an object.
# The statement x = 'foo' creates a symbolic name x that refers to the string object 'foo'.

# In a program of any complexity, you’ll create hundreds or thousands of such names,
# each pointing to a specific object. How does Python keep track of all these names
# so that they don’t interfere with one another?

# You can think of a namespace as a dictionary in which the keys are the object names and
# the values are the objects themselves.
# Each key-value pair maps a name to its corresponding object.

# In a Python program, there are four types of namespaces:

# Built-In
# Global
# Enclosing
# Local

# These have differing lifetimes. As Python executes a program, it creates namespaces as
# necessary and deletes them when they’re no longer needed. Typically, many namespaces will
# exist at any given time.

# Buildin Namespace
# The built-in namespace contains the names of all of Python’s built-in objects.
# These are available at all times when Python is running. You can list the objects in the
# built-in namespace with the following command:

print(dir(__builtins__))
# The Python interpreter creates the built-in namespace when it starts up.
# This namespace remains in existence until the interpreter terminates.















# Since Python is a dynamically-typed language, variables in Python come into existence when you
# first assign them a value. On the other hand, functions and classes are available after you
# define them using def or class, respectively. Finally, modules exist after you import them.




