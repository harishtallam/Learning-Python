"""
There is a lot of work in building an iterator in Python.
We have to implement a class with __iter__() and __next__() method, keep track of internal states, and
raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators.
All the work we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate
over (one value at a time).
"""

# Example 1

def topten():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


values = topten()

print(values.__next__())
print(values.__next__())
print()
for i in values:
    print(i)


# Example 2
def sqrt_topten():

    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


sqrt_values = sqrt_topten()
for x in sqrt_values:
    print(x)
