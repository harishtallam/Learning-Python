# Constructor will always executes irrespective of other code

class Computer:

    def __init__(self, cpu, ram):  # constructor
        # the init will called depends upon number of objects
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is:", self.cpu, self.ram)


com1 = Computer("16gb", "8TB")  # Object creation 1, also calls via init
com2 = Computer("8GB", "4TB")  # Object creation 2, also calls via init

print()

com1.config()
com2.config()
