"""
1. Lambda is also called anonymous functions
2. A function without a name is called lambda
3. A function with "single expression of code" can be defined as a lambda/anonymous function to save number
   of lines of code
"""

# Example 1
f = lambda a: a * a
result = f(9)
print(result)

# Example 2
z = lambda x, y: x + y
result1 = z(2, 3)
print(result1)