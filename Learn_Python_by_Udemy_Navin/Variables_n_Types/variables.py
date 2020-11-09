
##################################
##### VARIABLES WITH NUMBERS #####
##################################

2 + 3 # Execute in python terminal or IDLE terminal
print (2+3)

x = 2
x + 2 # Execute in python terminal or IDLE terminal
print (x+2)

y = 3
x + y # Execute in python terminal or IDLE terminal
print (x+y)

x = 5 # Overwriting x variable
x + y
print (x)
print (x + y)

# _ print previous o/p
# Eg: _
# Eg: _  + y



##################################
##### VARIABLES WITH STRINGS #####
##################################

name = 'harish'
name # Execute in python terminal or IDLE terminal
print (name)

name + 'tallam' # Execute in python terminal or IDLE terminal
print (name + ' tallam')

# name ' tallam' # Execute in python terminal or IDLE terminal. 
# This will given an error as string requires '+' for concatenation
# print (name ' tallam')

## Indexing of String
###   0   1   2   3   4   5  ## From left to right
###   h   a   r   i   s   h
###  -6  -5  -4  -3  -2  -1  ## From right to left

print (name[0]); print(name[-1]); 
print (name[1]); print(name[-2]); 
print (name[2]); print(name[-3]); 
print (name[3]); print(name[-4]); 
print (name[4]); print(name[-5]); 
print (name[5]); print(name[-6]); 

print (name[0:3]) # prints 'har'
print (name[1:5]) # prints 'aris'
print (name[3:6]) # prints 'ish'
print (name[:3]) # prints 'har'
print (name[3:])  # prints 'ish'

print (name[3:10]) # In this case, it prints till the characters are available

# Trying to change string

# The below gives an error -- 'str' object does not support item assignment.
# This indicates string in python are immutable
# name[0:3] = 'har'

# In this case, to overwrite a particular string, we can split and concatenate with other string

new_name='youtube'
print(new_name[0:3] + ' me')
print('my ' + new_name[3:])

### Length of a string
print(len(new_name))