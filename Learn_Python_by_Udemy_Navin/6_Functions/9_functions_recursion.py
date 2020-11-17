# Recursion - Calling a function itself

import sys

# By default, the recursive function can be executed only 1000 times
print(sys.getrecursionlimit())  # This will give recursion limit

print(sys.setrecursionlimit(2000))  # Using this, we can overwrite recursion limit

print(sys.getrecursionlimit())  # Checking the recursion limit after overwriting it

# Example for understanding
i = 0


def greet():
    global i
    i += 1
    print("Hello", i)
    greet()


# Enable below just to understand the recursion
# greet()


# Example - 1
# Factorial using recursion
def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)


x = 5
result = fac(x)
print(result)
