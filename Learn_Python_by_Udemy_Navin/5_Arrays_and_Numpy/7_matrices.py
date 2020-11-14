from numpy import *

# Multi-dimensional Array
# Example 1
arr1 = array([
                [1, 2, 3],
                [4, 5, 6]
            ])
print(arr1)  # Prints array
print(arr1.dtype)  # Prints datatype of an array
print(arr1.ndim)  # Prints dimension of an array
print(arr1.shape)  # Prints number of rows and columns of an array
print(arr1.size)  # Gives size of an entire block


# Example 2
arr2 = arr1.flatten() # Multi-Dimensional to Single Dimensional array
print(arr2)

# Example 3
arr3 = array([
                [1, 2, 3, 4, 5, 6],
                [4, 5, 6, 7, 8, 9]
            ])
# print(arr3)
arr4 = arr3.reshape(3, 4)  # 3 rows and 4 columns. Converts to 3d array
print(arr4)

arr5 = arr3.reshape(2, 2, 3)
# Creates a 3d array which will have two - 2d arrays. And each 2 array will have 2 1d arrays

print(arr5)


"""
MATRICES IN PYTHON
"""
# Example 1
# We need to require to create an array everytime for a matrix. Refer examples from 2
mar1 = array([
                [4, 1, 2],
                [6, 9, 8]
            ])
m = matrix(mar1)
print(m)

# Example 2
mar2 = matrix('1, 2, 3; 4, 5, 6')
print(mar2)

# Example 3
mar3 = matrix('1, 4; 2, 5; 3, 6')
print(mar3)

# Example 4
mar4 = matrix('1, 4, 7; 2, 5, 8; 3, 6, 9')
print(diagonal(mar4)) # Gives diagonal
print(mar4.min())  # Gives minimum value in a matrix
print(mar4.max())  # Gives maximum value in a matrix

# Example 5
mar5 = matrix('1, 4, 7; 2, 5, 8; 3, 6, 9')
mar6 = matrix('2, 3, 7; 3, 6, 8; 4, 8, 9')
sum_mar = mar5 + mar6  # Sum of matrices
print(sum_mar)

multi_mar = mar5 * mar6
print(multi_mar)


"""
Assignment
1. Write a code to multiply 2 matrices using 2D array and using loops
"""
arm1 = array([

    [234, 456, 789, 475, 56, 23],
    [78, 98, 99, 66, 45, 67]
])

arm2 = array([
    [23, 45, 78, 75, 56, 23],
    [78, 98, 99, 66, 45, 67]
])

k = 0
for i in arm1:
    new_arr = arm1 * arm2
    print(new_arr, end='  ')
    k = +1
    break
