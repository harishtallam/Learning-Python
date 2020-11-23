"""
Types of variables in Oops:
1. Instance variable
    a. These needs to be created in __init__ method. As the object changes, the value gets changed
    b. These can be overridden per object
    c. Instance variables will store in instance namespace
2. Class Variables or Static Variables
    a. These needs to be created at class level
    b. If these are overridden, it will effect all the objects where ever these are used
    c. Class variables will store in class namespace
"""


class Car:
    # class or static variable
    # These gets stored in class namespace
    wheels = 4

    def __init__(self):
        # These are instance variables
        # These gets stored in instance namespace
        self.mil = 100
        self.com = "BMW"


c1 = Car()
c2 = Car()

print(c1.mil, c1.com)
print(c2.mil, c2.com)

# overwriting instance variable
c1.mil = 80
print()

# printing after overwriting instance variable
print(c1.mil, c1.com)
print(c2.mil, c2.com)

# Printing along with class variables
# We can use "c1" (object) or Car (class) to print class variables
print(c1.mil, c1.com, c1.wheels, Car.wheels)
print(c2.mil, c2.com, c2.wheels, Car.wheels)

# overwriting class variable, this will effect all the objects which uses this variable
Car.wheels = 5
print()

# Printing after overwriting class variable
print(c1.mil, c1.com, c1.wheels, Car.wheels)
print(c2.mil, c2.com, c2.wheels, Car.wheels)
