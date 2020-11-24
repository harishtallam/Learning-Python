
# Example 1
# This kind of swapping does not work as values are overridden
a = 5
b = 6

a = b  # 'a' becomes 6 from 'b'
b = a  # 'b' becomes 6 as 'a' was 6 due to previous assignment
a = b  # 'a' becomes 6 as 'b' was 6 due to previous assignment

print(a)
print(b)
print()

# Example 2
# The below example will work, but the only disadvantage is that new variable gets created which is -
# - unnecessary usage of memory from programming perspective view
a = 5
b = 6

temp = a
a = b
b = temp

print(a)
print(b)
print()


# Example 3
# This will work with an very small amount of increase in memory which is bits
a = 5
b = 6

a = a + b  # 11
b = a - b  # 5
a = a - b  # 6

print(a)
print(b)
print()


# Example 4
a = 5
b = 6

a = a ^ b  # 11
b = a ^ b  # 5
a = a ^ b  # 6

print(a)
print(b)
print()


# Example 5
# Best way of implementing "swapping values"
a = 5
b = 6

a, b = b, a

print(a)
print(b)
print()
