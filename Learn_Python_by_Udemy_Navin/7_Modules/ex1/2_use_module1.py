"""
Importing custom modules in pycharm:
https://stackoverflow.com/questions/28705029/pycharm-error-no-module-when-trying-to-import-own-module-python-script
"""

from ex1 import mycal

a = 3
b = 2

c = mycal.add_new(a, b)
print(c)