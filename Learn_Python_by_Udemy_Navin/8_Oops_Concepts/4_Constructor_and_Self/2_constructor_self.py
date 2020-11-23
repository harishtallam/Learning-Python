
# Example 2
class Computer:

    def __init__(self):
        self.name = "Harish"
        self.age = 33

    # overwriting default values - way 2 (using method/function)
    def update(self):
        self.age = 30


c1 = Computer()  # Object Creation - Computer() is an constructor which will call __init__ method internally
c2 = Computer()  # Object Creation - Computer() is an constructor which will call __init__ method internally

# overwriting values - way 1
# overwriting __init__
c1.name = "Tallam"
c1.age = 32

print(c1.name)
print(c2.name)

print(c1.age)
print(c2.age)

c1.update()  # this updates the age through update() method
print()

print(c1.age)
print(c2.age)
