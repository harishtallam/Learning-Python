##### Data types in python
# None - works like a "null"
# Numeric - int, float, complex and bool
# List
# Set
# Tuple
# String
# Range
# Dictionary


## Numerics
num = 5
print(type(num))

num1 = 2.5
print(type(num1))

num2 = 2 + 3j
print(type(num2))
print(num2)

# Converting float to int
num3 = 5.5
print(int(num3))

num4 = 6
print(float(num4))

# Converting int to complex
print(complex(num4))
print(complex(num3,num4))

# Bool
boo = num4 < num3
print(boo)
print(type(boo))

boo1 = num4 > num
print(boo1)
print(type(boo1))

print(int(True))
print(int(False))

# Sequence (List, Tuple, Set, String and Range)
lst = [10,5,9,13,18]
print(type(lst))

s = {10,5,9,13,18}
print(type(s))

t = (10,5,9,13,18)
print(type(t))

st = 'harish'
print(type(st))

# Python does not have char type like in other programming languages

print(range(10)) # Gives range
print(type(range(10)))

print(list(range(10))) # Lists range of the value

print(list(range(2,10)))
print(list(range(2,10,2)))


## Dictionary

dict = {'harish':'gnt', 'vyshu':'mrk', 'haashritha':'blr'}
print(dict.keys())
print(dict.values())

print(dict['harish'])
print(dict.get('vyshu'))