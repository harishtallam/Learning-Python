# Keyworded variable length arguments

# Example 1
# In case of multiple arguments with its variables, we need to define ** instead of * in function
# To understand this, lets pass data. the first arg will fall under name variable and rest as tuple
# Using this approach, we cannot print individually and also we cannot map key variable against args
def person(name, *data):
    print(name)
    print(data)


person('harish', 33, 'Bangalore', 9876543210)
# person('harish', age=33, city='Bangalore', mob=9876543210) # This will not work as the remaining args are in tuple


# Example 2
# This approach is keyworded variable length arguments
def person1(name, **data):
    print(name)
    # print(data)
    for a, b in data.items(): # It has to be iterated item by item
        print(a, b)


person1('harish', age=33, city='Bangalore', mob=9876543210)
