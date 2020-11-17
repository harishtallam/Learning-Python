"""
Python has an interesting feature called decorators to add functionality to an existing code.
This is also called metaprogramming because a part of the program tries to modify another part
of the program at compile time.

The use of decorator functions is that - we can overwrite the function using a new function over compile
time. The reason using new function is, we cannot touch the main function as it can be commonly used by
many other functions or objects
"""


# Example
# Here "dev" function is the main function
# smart_div is the new function where the inner function is meant to overwrite the main function

def div(a, b):
    print(a/b)


def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div = smart_div(div)
div(2, 4)
