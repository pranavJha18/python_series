# Strings
example_1 = "Hello, everyone"
example_2 = """
This comment
can span
several
lines.
"""
print(example_2)
# we have to be consistent with our choice of quotes...
# for example if we start with ' then we have to end with '

string_num = "5"
integer_num = 5
print(type(string_num), type(integer_num))
# an integer in quotes is a string and not an integer so we cannot perform any
# arithematic operation on it like addition or subtraction etc

# Lists
my_list = ["one", 2, "three"]
print(my_list)

# Tuples:-> it is an immutabale type
# i.e, we cannot change it's value after it's creation
my_tuple = ("Hello", 2, "you")
print(type(my_tuple))

just_int = 100
print(type(just_int))
int_tuple = (100,)
print(type(int_tuple))

# Index operator
s_string = "Python"
print(s_string[0])
print(len(s_string))
my_list = ["one", 2, "three"]
print(my_list[0])
print(my_list[len(my_list) - 1])
# The other way to print the last part of the above list is to use the negative
# number index; eg:my_list[-1] will print "n"
