"""
Different ways of creating an array
1. array()
2. linspace()
3. logspace()
4. arange()
5. zeros()
6. ones()
"""

from numpy import *

"""
 Type 1 - array()
"""
# example 1
arr = array([1, 4, 3, 2, 5])
print(arr)
print(arr.dtype)

# example 2
arr1 = array([3, 2, 1, 41, 4.5])  # as one of the value is float, rest follows the same
print(arr1)
print(arr1.dtype)

# example 3
arr2 = array([1, 4, 5, 2, 22], int)
print(arr2)
print(arr2.dtype)

# example 4
arr3 = array([1, 4, 5, 2, 22.5], int)
print(arr3)
print(arr3.dtype)

# example 5
arr4 = array([1, 4, 5, 2, 22], float)
print(arr4)
print(arr4.dtype)

"""
Type 2 - linspace()
"""

# Example 1
# 0 is starting number, 16 is ending number and 10 is number of parts between start & stop which is optional
lsp1 = linspace(0, 16, 10)
print(lsp1)

# Example 2
lsp2 = linspace(0, 15, 16)
print(lsp2)

# By default last value is 50 parts
# Example 3
lsp3 = linspace(0, 15)
print(lsp3)

"""
Type 3 - arange()
"""

# Example 1
# 0 is start number, 15 is end number and 2 is number of steps
ara1 = arange(1, 15, 2)
print(ara1)

"""
Type 4 - logspace()
"""

# Example 1
# In case of linspace, the difference between 2 numbers is always fixed.
# Whereas in case of logspace, the difference betwen 2 numbers is depends on log of it
lgsp1 = logspace(1, 40, 5)  # 10 raise to 1 -- 10 raise to 40 with 5 steps
print(lgsp1)
print('%.2f' %lgsp1[0])  # to print the specific syntax of the value
print('%.2f' %lgsp1[4])  # to print the specific syntax of the value

"""
Type 5 - zeros()
"""
# Example 1
zr1 = zeros(5)
print(zr1)

zr2 = zeros(5, int)
print(zr2)

"""
Type 6 - ones()
"""
# Example 1
on1 = ones(5)
print(on1)

# Example 2
on2 = ones(5, int)
print(on2)