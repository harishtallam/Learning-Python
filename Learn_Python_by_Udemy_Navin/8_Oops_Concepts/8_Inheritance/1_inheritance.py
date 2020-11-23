"""
Inheriting characteristics from parent to child is called Inheritance
3 types of Inheritance
1. Single level inheritance
2. Multi Level inheritance
3. Multiple Inheritance
"""


class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


# Single Level Inheritance
# Inheriting class A in class B
class B(A):
    def feature3(self):
        print("Feature 3 working")


# Multi Level Inheritance
# Inheriting Class B (which in-turn inherits class A) in class C
class C(B):
    def feature4(self):
        print("Feature 4 working")


class D:
    def feature5(self):
        print("Feature 5 working")


# Multiple Inheritance
# Inheriting different multiple classes into a class
class E(A, D):
    def feature6(self):
        print("Feature 6 working")


a1 = A()
a1.feature1()
a1.feature2()
print()

b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()

c1 = C()
c1.feature4()

d1 = D()
d1.feature5()

e1 = E()
e1.feature1()
e1.feature2()
e1.feature5()
e1.feature6()