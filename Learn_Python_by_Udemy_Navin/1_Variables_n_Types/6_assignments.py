##### From Section 1 - Introduction #####
# Who is the Founder of Python Language?
# Guido Van Russom
#########################################

## Variables Assignment
# Guess the output for below:
print(r'Telusko \n Rocks')
print('Telusko \n Rocks')

## Lists Assignment
# What's the output of -3 of "Telusko"
name = "Telusko"
print(name[-3])

## Tuples Assignment
# Delete elements (95,14,12)
nums=[25,36,95,14,12,26]
del nums[2:5]
print(nums)

"""
What is Mutability means?
Immutability:
    We can't change the value of variable of mutable data type once created. It means, we can delete the entire element using del operator, however we can't modify/delete items of the element.  Eg. str, tuple. i.e., It does not support item deletion.

Mutability:  It supports item deletion modification/deletion. Eg. list,set
"""

"""
Difference between Set and List?
1. Set is immutable, where as List is mutable
2. Set does not prints in sequence order, where as List does
3. Set cannot have repetitive values, where as List can
"""

"""
How to access help docs in Python?
In IDLE terminal:
>>> help()
> topics
> LISTS
> quit

or

>>> help('LISTS')
"""