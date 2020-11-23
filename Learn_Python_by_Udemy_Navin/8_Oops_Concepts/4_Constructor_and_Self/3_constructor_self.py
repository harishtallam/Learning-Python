
# Example 2
class Computer:

    def __init__(self):
        self.name = "Harish"
        self.age = 33

    # overwriting default values - way 2 (using method/function)
    def update(self):
        self.age = 30

    # compare function
    def compare(self, other): # self indicates c1 and other indicates other here
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 33
c2 = Computer()

# compare
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)

print(c1.age)
print(c2.age)
