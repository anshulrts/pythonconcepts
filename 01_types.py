# Numeric Types     :	int, float, complex
# Text Type         :	str
# Sequence Types    :	list, tuple, range
# Mapping Type      :	dict
# Boolean Type      :	bool
# Set Types         :	set, frozenset
# Binary Types      :	bytes, bytearray, memoryview
# None Type         :	NoneType

# We can get the type using type() function

# Eg
x = 5
print(type(x)) # <class 'int'>
y = 'abc'
print(type(y)) # <class 'str'>
# We can point to a new type
y = 10
print(type(y)) # <class 'int'>

# NoneType
z = None
print(type(z)) # <class 'NoneType'>

# String type
string1 = "This is a string"

print(f"Length of string1 is : {len(string1)}") # Length of string1 is : 16
print(f"First Character is : {string1[0]}") # First Character is : T
# Negative Indexing
print(f"Last Character is : {string1[-1]}") # Last Character is : g

# In Python, you can pack & unpack tuples.
# Eg
s1 = 1
s2 = 2
s3 = 3
s4 = 4
tt = (s1, s2, s3, s4)
print(tt) # (1, 2, 3, 4)

(x, y, z, a) = tt
print(x) # 1