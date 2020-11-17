"""
Types of Arguments for functions:
1. Position
2. keyword
3. Default
4. Variable Length
"""


# Position type
# Example 1
# Usually, we need to maintain the sequence for arguments which is positions
def person(name, age):
    print(name)
    print(age)


person('harish', 32)


# Keyword type
# Example 1
# If we do not know the sequence of arguments, we can follow below keyword based
def person1(name, age):
    print(name)
    print(age-5)  # reducing given age by 5


person1('harish', 32)  # this will work as we have followed sequence
# person1(32, 'harish')  # this will not work as the sequence is not followed and we cannot subtract -5 on name
person1(age=32, name='harish')  # this will work as we have passed values along with keys


# Default type
# Example 1
# Defaulting some variable values in function itself
def person2(name, age=18):
    print(name)
    print(age)


person2('harish')  # prints name along with default age given
person2('harish', 32)  # overwrites age
person2(age=32, name='harish') # overwrites age as well as positioned variables


# Variable Length
# Example 1
# In this example, the 1st value gets assigned to 'a' and rest of the values gets assigned to b as a tuple
# so that even if we do not know the no. of args, we can still pass many args
def add(a, *b):
    # print(a)
    # print(b)
    c = a
    for i in b:
        c = c + i

    print(c)


add(5, 9, 13, 18)


# Example 2
# In this example, all the values gets assigned to b as a tuple
# so that even if we do not know the no. of args, we can still pass many args
def add1(*b1):
    # print(b)
    for j in b1:
        c1 = c1 + j

    print(c1)


add(5, 9, 13, 18)
