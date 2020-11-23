# MRO - Method Resolution Order

class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B():

    def __init__(self):
        print("In B init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):
    def __init__(self):
        print("in C Init")
        # As class C has 2 parents; as per MRO - it takes from left to right for super init call
        # Hence, it calls class A init
        super().__init__()

    # Calling method of a super class
    def feat(self):
        super().feature2()

a1 = C()
# MRO logic is applicable for methods also
a1.feature1()
print()
# Calling method of a super class
a1.feat()
