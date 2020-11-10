############################################################
########## ADDRESS OF A VARIABLES, STRINGS, ETC. ###########
############################################################

n = 1
print(id(n))

name1 = 'harish'
print(id(name1))

a = 10
b = a # assigning a to b
print(id(a))
print(id(b)) # The address will be same for a & b as python is memory efficient
print(id(10)) # The address will be same as the value is same for a, b and direct 10; python is memory efficient

a = 5
print(id(a)) # this will give new address
print(id(b)) # this will give old address only as the new assignment is not done

b = 1
print(id(b)) # this will give new address

print(type(a))
print(type(b))

PI = 3.14
print(type(PI))