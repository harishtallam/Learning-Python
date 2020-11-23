
class Computer:
    def config(self):
        print("i5", "16gb", "8TB")


com1 = Computer()
com2 = Computer()

print(type(com1))
print(type(com2))

print()

Computer.config(com1)
Computer.config(com2)
print()
com1.config()
com2.config()
