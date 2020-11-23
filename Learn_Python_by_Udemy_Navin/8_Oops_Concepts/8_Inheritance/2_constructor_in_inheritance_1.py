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
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


# This will print default constructor from class A
a1 = A()

"""
--> This will also print default constructor from class A thru class B
--> Sub-class can access all the features of super class, 
    but super class cannot access any feature of sub-class
--> As the constructor is not available in class B, the super class constructor gets executed
"""
a1 = B()
