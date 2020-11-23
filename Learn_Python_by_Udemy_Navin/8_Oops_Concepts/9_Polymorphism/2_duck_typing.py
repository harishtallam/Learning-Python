"""
Duck Typing:
Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc.
where the type or the class of an object is less important than the method it defines.
Using Duck Typing, we do not check types at all.

Instead, we check for the presence of a given method or attribute.

The name Duck Typing comes from the phrase:
“If it looks like a duck and quacks like a duck, it’s a duck”
"""


class VisualStudio:

    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Executing")


class PyCharm:

    def execute(self):
        print("Compiling")
        print("Executing")

class Laptop:

    def code(self, ide):
        ide.execute()


ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)
print()

ide = VisualStudio()

"""
To understand in thsi example, it doesn't matter which IDE we are passing here, the IDE must have execute()
method which is a common feature for IDEs like in "Duck"
"""
lap1.code(ide)