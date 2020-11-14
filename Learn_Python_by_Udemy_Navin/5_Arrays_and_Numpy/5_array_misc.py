from numpy import *

# Some miscellaneous examples

# Example 1
# Using numpy, we can some value to each number in a array. Usually, we need to iterate each index and add
arr1 = array([5, 3, 2, 1, 9])
arr1 = arr1 + 5
print(arr1)

# Example 2
# Add 2 arrays. Also called "Vectorized Operation"
arr2 = array([5, 3, 2, 1, 9])
arr3 = array([5, 4, 3, 2, 1])
arrNew = arr2 + arr3
print(arrNew)

# Example 3
# Concatenate two arrays
# Used arrays from "Example 2"
print(concatenate([arr2, arr3]))

# Example 4
# Some miscellaneous examples
arr4 = array([5, 3, 2, 1, 9])

print(sum(arr4))
print(sin(arr4))
print(cos(arr4))
print(log(arr4))
print(min(arr4))
print(max(arr4))
print(sqrt(arr4))
print(sort(arr4))

