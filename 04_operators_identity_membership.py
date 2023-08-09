# Python language offers some special types of operators like
# the identity operator
# and the membership operator.

# Identity Operators
# In Python, is and is not are used to check if two values are located on the same part of the memory.
# Two variables that are equal does not imply that they are identical.

x1 = 5
y1 = 5
x2 = 'abc'
y2 = 'abc'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is y1)
print(x2 is y2)
print(x3 is y3)
print(x3 == y3)
# x3 and y3 are lists. They are equal but not identical.
# It is because the interpreter locates them separately in memory although they are equal.




# Membership Operator
# In Python, in and not in are the membership operators.
# They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
# In a dictionary we can only test for presence of key, not the value.

x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False
