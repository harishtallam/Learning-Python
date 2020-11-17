"""
global <<variable>>
globals()['<<variable>>']
"""

# Example 1
# General understanding of global and local variable

a = 10  # Global variable


def something():
    a = 5  # Local variable
    # This will create a new variable a locally. That means, global variable is not being reused here
    # But still, we can use global variable inside a function but the thing is global value will be accessed
    print(id(a))
    print("Inside a function: ", a)


something()

print(id(a))
print("Outside a function: ", a)
print()

# Example 2
# global keyword
a1 = 10  # Global variable


def something1():
    global a1  # Using this, the value of "a1" gets changed outside and inside of the function
    a1 = 25  # However local variable will be considered as local because of the "global" keyword
    # because of this, we cannot achieve local variable assignment
    print(id(a1))
    print("Inside a function a1: ", a1)


something1()

print(id(a1))
print("Outside a function a1: ", a1)

# Example 3
# globals()['<<variable>>']

a2 = 10
print(id(a2))


def something2():
    a2 = 5

    x = globals()['a2']
    print(id(x))  # The address of 'x' should also refer to address of a2.
    # In addition, the variable is being locally also with same address
    print("inside a function a2: ", a2)

    globals()['a2'] = 15  # overwriting variable


something2()
print("outside a function a2:", a2)
