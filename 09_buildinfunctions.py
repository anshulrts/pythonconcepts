# 1. any()
# syntax - any(iterable)
# The any() function returns True if any element of an iterable is True. If not, it returns False.
# 0, False, empty is considered as falsy value
# Eg,
print("------------------1. any()---------------------")
lst = [0 ,1, 2]
print(any(lst)) # True since 1,2 are true
lst = []
print(any(lst)) # False
lst = [0, False]
print(any(lst)) # False
d = {0: 'True'}
print(any(d)) # False, since any checks Keys in case of dictionaries.
d = {0: True, 10: "Value"}
print(any(d))

# 2. all()
# Just opposite of any(), The all() function returns True if all elements in the given iterable are true.
# If not, it returns False.
# 1 difference is that in case of empty list/dict, we get True
print("------------------2. all()---------------------")
ls = []
print(all(ls)) # True
ls = [1, 2, 3]
print(all(ls)) # True
ls = [0, 1]
print(all(ls)) # False

# 3. bool()
# The bool() method returns:
# False - if argument is empty, False, 0 or None
# True - if argument is any number (besides 0), True or a string

# 4. chr()
# The chr() method converts an integer to its unicode character and returns it.
print("------------------4. chr()---------------------")
print(chr(97)) # a
print(chr(100)) # d

#5. int()
# Eg
print("------------------5. int()---------------------")
print(int(123.97)) # 123
# print(int('A')) Invalid argument for int()
# Use ord() to get unicode equivalent
print(ord('A')) # 65

# 6. enumerate()
# The enumerate() function adds a counter to an iterable and returns it (the enumerate object).
# The returned object is an enumerate object.
# You can convert enumerate objects to list and tuple using list() and tuple() functions respectively.
# Eg
print("------------------6. enumerate()---------------------")
lang = ["python", "C#", "Java"]
enumerate_lang = enumerate(lang)
print(type(enumerate_lang))
print(list(enumerate_lang))
# Looping over Enumerate
grocery = ['bread', 'milk', 'butter']
for item in enumerate(lang): # Note- not for item in enumerate_lang: -> This is an object, not enumerator
  print(item)
print()
for count, item in enumerate(lang):
  print(count, item)

# map() and filter()
# Map() and filter() functions are higher-order functions in Python.
# A higher-order function is referred to a function whose attributes or parameters
# are in the form of a function, and it returns output in the form of a function only.

# 7. map()
# The map () function is considered a replacement for the python for loop.
# We can apply the same function to all the items which are passed as an argument to the map() function.
# Syntax of map() function is very easy
# map(function name, iterable(list of items))
print("------------------7. map()---------------------")
def double_num(n):
  return 2*n

nums = [10,20,30,40]
print("Double using map() : ", list(map(double_num, nums)))
# Using “for loop” may make the problem harder to solve in some situations.
# For example, if we want to use the same function on two different lists of items,
# we need to use “for loop” twice. On the other hand, this problem can be solved with
# just one line of code using the map() method. We can give the map() method many different
# things in Python. Let’s see the syntax and example.
# map(function_name,iterable_1,iterable_2,iterable_3) 
def Add_num(a,b,c):
  return a+b+c
Num1= (2,4,6,8,10)
Num2= (3,6,9,12,15)
Num3= (4,8,12,16,20)
Result = map(Add_num, Num1,Num2,Num3)
print(Result) # <map object at 0X......>
Output = list(Result)
print(Output)


# 8. filter()
# The filter() function selects elements from an iterable (list, tuple etc.)
# based on the output of a function.
# The function is applied to each element of the iterable and if it returns True,
# the element is selected by the filter() function.
# The filter() function returns an iterator.
# Note: You can easily convert iterators to sequences like lists, tuples, strings etc.
print("------------------8. filter()---------------------")
def check_even(num):
  if num % 2 == 0:
    return True
  return False

numbers = [0, 1, 2, 3, 4, 5]
even_nums = list(filter(check_even, numbers))
print(even_nums)

# 8. lambda
# With map & filter functions, you can use lambda instead of writing the function.
# In the above example, instead of defining check_even, you can directly define a
# lambda func
# Eg
print(list(filter(lambda i: i%2==0, numbers)))

# 9. next() and iter()
# Iterators are methods that iterate collections like lists, tuples, etc.
# Using an iterator method, we can loop through an object and return its elements.
# Technically, a Python iterator object must implement two special methods,
# __iter__() and __next__(), collectively called the iterator protocol.

# In Python, we can use the next() function to return the next item in the sequence.

# Eg
# define a list
my_list = [4, 7, 0]
# create an iterator from the list
iterator = iter(my_list)
# get the first element of the iterator
print(next(iterator))  # prints 4
# get the second element of the iterator
print(next(iterator))  # prints 7
# get the third element of the iterator
print(next(iterator))  # prints 0
# print(next(iterator))  throws StopIteration Exception

# The syntax of next() is:
# next(iterator, default)
# iterator - next() retrieves next item from the iterator
# default (optional) - this value is returned if the iterator is exhausted (there is no next item)

# We can add conditions to next()
# Eg
nums = [-4,-1,0,4]
try:
  x = next(x for x, val in enumerate(nums) if val >= 0)
except StopIteration as e:
  x = 0

