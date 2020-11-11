## List any 5 funtions from math module and how it works?
import math
print(math.sqrt(4))
print(math.floor(3.2))
print(math.ceil(3.2))
print(math.degrees(1)) # converts radians to degrees
print(math.fabs(2.13)) # returns absolute value of the float


"""
Write a code to find the cube of the number. Take input from the user using input() and also using command line
"""

# Solution 1
import math
print(math.pow(3,3))

# Solution 2
x = int(input("Enter the number: "))
print(math.pow(x,3))

# Solution 3
# Need run like --> py filename.py
import sys
y = int(sys.argv[1])
print(math.pow(y,3))