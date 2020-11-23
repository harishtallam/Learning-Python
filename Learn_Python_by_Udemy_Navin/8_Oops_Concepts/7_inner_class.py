"""
Inner Class:
--> Class inside a class
-->
"""


class Student:

    # Constructor
    def __init__(self, name, rollnum):
        self.name = name
        self.rollnum = rollnum
        # Declaring inner class as variable
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollnum)
        # calling method of inner class
        self.lap.show()

    # Inner class
    class Laptop:

        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Harish", 5)
s2 = Student("Vyshnavi", 9)

# Way 1 of printing data (by object)
print(s1.name, s1.rollnum)
print(s2.name, s2.rollnum)
print()

# Way 2 of printing data (by method)
# s1.show()
# s2.show()
# print()

lap1 = s1.lap
lap2 = s2.lap

# different object creation
print(id(lap1))
print(id(lap2))
print()


"""
We can create object of inner class inside the outer class

or

We can create object of inner class outside the outer class provided we use outer class name to call it
"""
# Object creation for inner class (Laptop) through outer class (Student)
# lap1 = Student.Laptop()
# lap2 = Student.Laptop()

s1.show()
