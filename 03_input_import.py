# The actual syntax of the print function accepts 5 parameters
# print(object= separator= end= file= flush=)
# Here,
# object - value(s) to be printed
# sep (optional) - allows us to separate multiple objects inside print().
# end (optional) - allows us to add add specific values like new line "\n", tab "\t"
# file (optional) - where the values are printed. It's default value is sys.stdout (screen)
# flush (optional) - boolean specifying if the output is flushed or buffered. Default: False

# Eg
x = "Happy New Year"
y = "2023"

print(x) # Happy New Year
print(y) # 2023
# In the above example, the print() statement only includes the object to be printed.
# Here, the value for end is not used. Hence, it takes the default value '\n'.
# So we get the output in two different lines.

print(x, end=' ')
print(y)
# Happy New Year 2023

print(x, y, "###",sep='! ') # Happy New Year! 2023! ###



# Concatenate String
print(x + " " + y) # Happy New Year 2023



# Python Input
prompt = "Enter a number "
abc = input(prompt)
print(type(abc)) # <class 'str'>
xyz = int(abc) # You get ValueError here if you didn't enter an integer
print(type(xyz)) # <class 'int'>