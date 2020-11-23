
# Example 1
class Computer:
    # We cannot maintain a empty class, hence mentioned pass or at least can write some print statement
    pass


c1 = Computer()  # Object Creation - Computer() is an constructor which will call __init__ method internally
c2 = Computer()  # Object Creation - Computer() is an constructor which will call __init__ method internally

# Every time we run this code, this creates a new object with new address for each object
print(id(c1))
print(id(c2))

# The size of the object depends upon number and size of variables
# Constructor is responsible to calculate and allocate the memory to an object
