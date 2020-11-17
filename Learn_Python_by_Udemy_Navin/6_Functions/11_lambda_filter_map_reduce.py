"""
filter()
map()
reduce()
"""


# Example - filter with lambda
# filter - This offers an elegant way to filter out all the elements of a sequence “sequence”,
#  -- for which the function returns True
# Instead of writing a named function, we can define filter lambda
def is_even(n):
    return n % 2 == 0


num = [1, 2, 3, 5, 6, 9, 10, 13, 16, 18]

# Here
even = list(filter(is_even, num))
print(even)

even1 = list(filter(lambda n: n % 2 == 0, num))
print(even1)


# Example - map with lambda
# map does an operation that gives final result
# The map() function in Python takes in a function and a list as an argument.
# The function is called with a lambda function and a list and a new list is returned which contains
# -- all the lambda modified items returned by that function for each item
def update(n):
    return n * 2


# calling named function
doubles = list(map(update, even1))
print(doubles)


# using lambda
doubles1 = list(map(lambda n: n * 2, even1))
print(doubles1)


# Example - reduce with lambda
# reduce belongs to a module functools
# reduce does summing of all values
# The function is called with a lambda function and an iterable and a new reduced result is returned.
# -- This performs a repetitive operation over the pairs of the iterable
from functools import reduce


def add_all(a, b):
    return a + b


sums = reduce(add_all, doubles1)
print(sums)

sums1 = reduce(lambda a, b: a + b, doubles1)
print(sums1)