"""
Iterators are objects that can be iterated upon. In this tutorial, you will learn how iterator works
and how you can build your own iterator using __iter__ and __next__ methods.

Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions,
generators etc. but are hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. An object which will return data,
one element at a time.

Technically speaking, a Python iterator object must implement two special methods, __iter__() and __next__(),
collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most built-in containers in Python
like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.

"""

nums = [9, 10, 6, 5]

# Usually to print above array, we need to use for or while loop like below

for i in nums:
    print(i)

print()

# or by using index
print(nums[0])
print(nums[2])
# print(nums[5]) # This would give index out of bound exception

print()

# To avoid such, we have inbuilt functions in python - iter(), __next__() and next()

# iter() will not give all the values, it will give only one value at a time
it = iter(nums)

# iter function has inbuilt __next__() will give the first/next value
print(it.__next__())
print(it.__next__())

# another one is next() which again works like iter
print(next(it))

print()
#####################################################################################


class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()

# print(values.__next__())
for i in values:
    print(i)
