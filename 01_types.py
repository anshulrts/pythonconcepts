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
print(type(x))
y = 'abc'
print(type(y))
# We can point to a new type
y = 10
print(type(y))

# NoneType
z = None
print(type(z))

# String type
string1 = "This is a string"

print(f"Length of string1 is : {len(string1)}")
print(f"First Character is : {string1[0]}")
# Negative Indexing
print(f"Last Character is : {string1[-1]}")