# Basic concepts of python
print("Hello World! Let's be consitent!!")

message = "Please be consistent!"
print(message)

# Type conversion
print(3.14, int(3.14), int(3.9999), int(-3.99), int(21), int("245"))
print(float(2), float("89.09"), float("90"))
print(str(124), str(534.4))

# val = 34 + 4
# print("The value of val is: " + val)
# This will produce error as to concatinate an int or a float with a string, we have to convert them to string first

val = 34 + 4
print("The value of val is: " + str(val))

# Variables
# variables conists of name, type, value and size
# In python we don't need to provide type and size of a variable
my_name = "Golu"  # It is called variable assignment
print(my_name)
# we always link the variable name from the left to a value on the right with '=' sign
# "Golu" = my_name is invalid
