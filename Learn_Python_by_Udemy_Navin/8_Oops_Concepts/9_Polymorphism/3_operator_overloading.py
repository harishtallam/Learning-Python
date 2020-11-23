"""
Operator Overloading means giving extended meaning beyond their predefined operational meaning.
For example operator + is used to add two integers as well as join two strings and merge two lists.
It is achievable because ‘+’ operator is overloaded by int class and str class.
You might have noticed that the same built-in operator or function shows different behavior
for objects of different classes, this is called Operator Overloading.
"""

# Python program to show use of  + operator for different purposes.

print(1 + 2)

# concatenate two strings
print("Harish"+"For")

# Product two numbers
print(3 * 2)

# Repeat the String
print("Harish "*4)

print()
print()
#################################
###### OPERATOR OVERLOADING #####
#################################


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # operator overloading
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        n3 = Student(m1, m2)

        return n3

    # operator overloading
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    # operator overloading
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(85, 94)
s2 = Student(63, 96)

s3 = s1 + s2

print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print()
print(s1)
print(s2)
