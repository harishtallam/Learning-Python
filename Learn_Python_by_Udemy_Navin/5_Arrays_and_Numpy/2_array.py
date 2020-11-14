# Inserting an element in array
from array import *

arr = array('i', [])  # Empty array
n = int(input("Enter the length of the array: "))
for i in range(n):
    x = int(input("Enter the value for the array: "))
    arr.append(x)

print(arr)

# Searching an element in an array
val = int(input("Enter the value to search: "))
count = 0
for e in arr:
    if e == val:
        print(count)  # this will print the index basis on the count variable
        break
    count += 1

print(arr.index(val))  # this will print the index basis on the index function

##########################
# Assignment
# 1. Create an array with 5 values and delete the value at index number 2 without built-in function

from array import *

arr1 = array('i', [1, 3, 2, 5, 4])
print(arr1)
for i in range(5):
    if i == 2:
        continue
    print(arr1[i])

#  2. Write a code to reverse an array without any in built function
arr2 = array('i', [13, 52, 10, 42, 5])
print(arr2)
print(arr2[::-1])  # Sol 1

# Sol 2
x = array('i', [1, 2, 3, 4, 5])
print(x)

y = array(x.typecode, (a for a in x))
counter = len(x) - 1
for i in x:
    y[counter] = i
    counter -= 1

print(y)
