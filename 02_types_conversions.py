# Python Type Conversions
# 2 types
# 1. Implicit (automatic)
# 2. Explicit (Deliberate cast(change))

# Implicit
x = 10
y = 1.23
z = x + y
print(f"Value : {z}") # 11.23
print(f"Type : {type(z)}") # Python always convert smaller type to bigger one to avoid data loss
# Type : <class 'float'>


# Explicit - Also called as Type Casting
# We get a TypeError when we try to add a str and int directly, because implicit doesn't work here
x = 10
y = '12'
z = x + int(y)
print(f"Value : {z}") # Value : 22
print(f"Type : {type(z)}") # Type : <class 'int'>

x = 10
y = 1.23
z = x + int(y)
print(f"Value : {z}") # Value : 11
print(f"Type : {type(z)}") # Type : <class 'int'>
# Note - There might be a data loss during explicit conversion