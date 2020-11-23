"""
Method overriding:

Method overriding is an ability of any object-oriented programming language that allows a
subclass or child class to provide a specific implementation of a method that is already
provided by one of its super-classes or parent classes. When a method in a subclass has the same name,
same parameters or signature and same return type(or sub-type) as a method in its super-class,
then the method in the subclass is said to override the method in the super-class.

"""


class A:

    def show(self):
        print("in A show")


class B(A):
    # pass
    def show(self):
        print("in B show")


s1 = A()
# run this by not maintaining any "show" method in class B and also keep "pass" in class B
s1.show()

print()
s1 = B()
s1.show()

