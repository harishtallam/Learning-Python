"""
Importing custom modules in pycharm:
https://stackoverflow.com/questions/28705029/pycharm-error-no-module-when-trying-to-import-own-module-python-script
"""

from ex1.mycal import *

a = 3
b = 2

c = add_new(a, b)
print(c)