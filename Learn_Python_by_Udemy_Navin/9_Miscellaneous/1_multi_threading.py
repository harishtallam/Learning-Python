from time import sleep
from threading import *


# class with main thread
class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(1)


# class with main thread
class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")
            sleep(1)


hello = Hello()
hi = Hi()

hello.start()
sleep(0.2)
hi.start()

hello.join()
hello.join()

print("Bye")
