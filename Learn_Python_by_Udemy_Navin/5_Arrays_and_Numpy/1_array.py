# Arrays are similar to lists with only difference is that the values in arrays must of be same data type

"""

|#####################################################################|
| Type Code |     C Type     |    Python Type    | Min. Size in Bytes |
|#####################################################################|
|    'b'    | Signed char    |       int         |          1         |  
|    'B'    | Unsigned char  |       int         |          1         |
|    'u'    | Py_UNICODE     | Unicode Character |          2         |
|    'h'    | Signed short   |       int         |          2         |
|    'H'    | Unsigned short |       int         |          2         |
|    'i'    | Signed int     |       int         |          2         |
|    'I'    | Unsigned int   |       int         |          2         |
|    'l'    | Signed long    |       int         |          4         |
|    'L'    | Unsigned long  |       int         |          4         |
|    'f'    | float          |       float       |          4         |
|    'd'    | double         |       float       |          8         |
|######################################################################

"""

# Example 1
import array as arr

vals = arr.array('i', [1, 4, 1, 41])
print(vals)

# Example 2
from array import *

vals1 = array('i', [2, 2, 5, 1, 5])
print(vals1)

# Example 3
# vals2 = array('i',[1,5,2,3.2,4]) # This will not work as float value is defined for integer array
# print(vals2)

# Example 4
vals3 = array('i', [4, 2, -1, 3, 2])
print(vals3)

# Example 5
# vals4 = array('I',[4,2,-1,3,2]) # This will nto work as "I" - unsigned int is defined
# print(vals4)

# Example 6
vals5 = array('i', [2, 6, 4, 1, 5])
print(vals5.buffer_info())  # This gives address and size of an array
print(vals5.typecode)

# Example 7
vals5.reverse()  # reverses the array
print(vals5)

# Example 8 - print indexes of an array
print(vals5[0])
print(vals5[2])

# Example 9 - Iterate and print indexes of an array by assuming the range
for i in range(5):
    print(vals5[i])

# Example 10 - Iterate and print indexes of an array dynamically
for i in range(len(vals5)):
    print(vals5[i])

# Example 11 - Works like example 10
for i in vals5:
    print(i)

# Example 12 - With unicode - character
vals6 = array('u', ['a', 'i', 'e', 'o', 'u'])
print(vals6)
for e in vals6:
    print(e)

# Example 13 - Copying an array from one to another
vals7 = array('i', [1, 2, 3, 4, 5])
print(vals7)
newArr = array(vals7.typecode,
               (a for a in vals7))  # considers typecode of a previous array while copying using for loop
for new in newArr:
    print(new)

# Example 14 - Considers typecode of a previous array while copying by doing square root using for loop
newArr = array(vals7.typecode, (a * a for a in vals7))
for new in newArr:
    print(new)

# Example 15 - Same as example 14 using while loop
while i < len(newArr):
    print(newArr[i])
    i += 1

##########################
# Assignments
# 1. Write a code to sort the array in ascending order
# Sol 1:
vals8 = array('i', [2, 1, 4, 5, 3])
print(sorted(vals8))

# Sol 2:
b = sorted(vals8)
for a in b:
    print(a)

# 2. Write a code to find a factorial of given number
import math

a = int(input("Enter the number for factorial: "))
print(math.factorial(a))
