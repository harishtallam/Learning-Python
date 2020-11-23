"""
Method Overloading:

Like other languages (for example method overloading in C++) do, python does not supports method overloading
by default. But there are different ways to achieve method overloading in Python.

The problem with method overloading in Python is that we may overload the methods but can only use the
latest defined method.
"""


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Method overloading possible logic
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a

        return s


s1 = Student(85, 94)

print(s1.sum(5, 9, 13))
print()
print(s1.sum(5, 9))
print()
print(s1.sum(5))
