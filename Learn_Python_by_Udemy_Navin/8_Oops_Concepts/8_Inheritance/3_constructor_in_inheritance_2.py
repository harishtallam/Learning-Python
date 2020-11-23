class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


# Single Level Inheritance
# Inheriting class A in class B
class B(A):
    def __init__(self):
        print("In B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


# This will print default constructor from class A
a1 = A()

# Compare with example from 2_constructor_in_inheritance_1.py
# If the constructor is available for the class B (which we are executing), only that constructor
# will be executed
a1 = B()
