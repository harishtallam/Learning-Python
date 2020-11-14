# Understanding Shallow and Deep Copy
from numpy import *

arr1 = array([5, 3, 2, 1, 9])

arr2 = arr1  # Copying arr1 to arr2

print(arr1)
print(arr2)

# arr1 and arr2 will have same addresses as the array is being copied
# This is also called aliasing
# As the address is same, the value in array can be modified by either arr1 or arr2
print(id(arr1))
print(id(arr2))

"""
Shallow copy
"""
arr3 = array([5, 3, 2, 1, 9])
arr4 = arr3.view()  # This will create a new array with same content and different address

print(arr3)
print(arr4)

# arr3 and arr4 will have different addresses
print(id(arr3))
print(id(arr4))

# Lets change one value in array and understand how shallow copy works
arr3[1] = 4

# Since we are doing shallow copy,
# the new value will reflect in both the arrays arr3 and arr4 even the address is different
print(arr3)
print(arr4)
print(id(arr3))
print(id(arr4))

"""
Deep copy
"""
arr5 = array([5, 3, 2, 1, 9])
arr6 = arr5.copy()  # This will create a new array with same content and different address

print(arr5)
print(arr6)

# arr5 and arr6 will have different addresses
print(id(arr5))
print(id(arr6))

# Lets change one value in array and understand how deep copy works
arr5[1] = 4

# Since we are doing deep copy,
# the new value will reflect in the array - arr3 only where it is changed
print(arr5)
print(arr6)
print(id(arr5))
print(id(arr6))

"""
Assignments
"""
# 1. Write a code to add 2 arrays using for loop
a1 = array([1, 2, 3, 4, 5])
a2 = array([6, 7, 8, 9, 0])
for i in range(len(a1)):
    a1[i] = a1[i] + a2[i]
print(a1)

# 2. Write a code to find the maximum number of an array without built-in function
a3 = array([10, 7, 9, 1, 0])
x = a3[0]
for j in range(1, len(a3)):
    if a3[j] > x:
        x = a3[j]
print(x)
