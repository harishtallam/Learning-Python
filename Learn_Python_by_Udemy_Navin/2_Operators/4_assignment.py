"""
Q: Name any four dataypes with definition?
"""

# Assignment basis on operators
# https://www.udemy.com/course/python-tutorials-for-by-navinreddy/learn/lecture/17101398#questions
a = 15
b = 12
x = (a // 4 + b ** 3) < 2000 and (b % 4 != 0)
print(x)

"""
(a//4+b**3)<2000 results into TRUE.
(b%4!=0) results into FALSE as b%4==0.
so (TRUE and FALSE) = FALSE.
so answer is FALSE
"""

# Guess the O/P for the following:

print(7<<2)
print(125|265)
print(652^125)
print((288<<2) >> (26 // 6))