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
