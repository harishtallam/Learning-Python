
class Computer:

    def __init__(self):
        # the init will called depends upon number of objects
        print("in init")

    def config(self):
        print("i5", "16gb", "8TB")


com1 = Computer()  # Object creation 1 basis on init
com2 = Computer()  # Object creation 2 basis on init

print()

com1.config()
com2.config()
