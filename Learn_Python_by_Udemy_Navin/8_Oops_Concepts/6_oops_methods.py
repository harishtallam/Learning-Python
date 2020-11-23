"""
Types of Methods:
1. Instance methods
    a. Accessor methods or "Getters"
        --> To access value, this needs to be used
        --> a separate accessor method or getter is required for each variable
    b. Mutator methods or "Setters"
        --> To change a value, this needs to be used
        --> a separate mutator method or setter is required for each variable
2. Class methods
3. Static methods
"""


class Student:

    # Class or Static variable
    School = "Tallam"

    # Constructor
    def __init__(self, m1, m2, m3):
        # Instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    """
    # Accessor methods or "getters
    def getResult(self):
        return self.m1

    # Mutator methods or "setters"
    def setResult(self, v1):
        self.m1 = v1
    """

    # Class method
    @classmethod
    def getSchoolName(cls):
        return cls.School

    # Static method
    @staticmethod
    def info():
        print("This is student")


s1 = Student(45, 63, 81)
s2 = Student(54, 72, 90)

# Printing Instance variables via instance methods
print(s1.avg())
print(s2.avg())
print()

# Printing class variable via class method
print(Student.getSchoolName())
print()

# Printing static method
Student.info()
