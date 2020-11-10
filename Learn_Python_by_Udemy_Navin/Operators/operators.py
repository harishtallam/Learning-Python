"""
Types of operators in Python:
1. Arithmetic Operators
2. Assignment Operators
3. Relational Operators
4. Logic Operators
5. Unary Operators
"""
##########################################################
## Arithmentic Operators
x = 2
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

##########################################################
## Assignment Operators
a = 2 # Assignment operator
a = a + 2  # Assignment operator
print(a)

b = 3
b += 3 # 3 + 3 = 6
print(b)
b *= 3 # 6 * 3 = 18
print(b)
b -= 3 # 18 - 3 = 15
print(b)
b /= 3 # 15 / 3 = 5
print(b)
b %= 5 # 5.0 % 5 = 0.0
print(b)

c,d = 5,6
print(c)
print(d)
print(c + d)

##########################################################
## Unary Operators
n = 7
print(n)
print(-n) # Negation
n = -n # Negation
print(n)

##########################################################
## Relational Operators
## For comparsion

e,f = 8,9
print(e < f)
print(e > f)

## Check the value is same or not
print(e == f) # Compare

g,h=10,10
print(g == h)

print(e <= f)
print(e >= f)
print(g <= h)
print(g >= h)

print(e != f)
print(g != h)


##########################################################
## Logical Operators

a = 5
b = 4
print(a < 8 and b < 5)
print(a < 8 and b < 2)

print(a < 8 or b < 5)
print(a < 8 or b < 2)
print(a > 5 or b < 2)

t = True
print(t)
print(not t) # Negation