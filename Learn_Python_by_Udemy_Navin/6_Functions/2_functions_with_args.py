
# Example 1
def update(x):
    x = 8
    print(x)


update(10)  # Here, even after passing 10 as an argument. value 8 is overwritten in function


# Example 2
def update(x):
    x = 8
    print("x: ", x)


a = 10
update(a)
print("a: ", a)


# Example 3
def update(x1):
    print(id(x1))
    x1 = 8
    print(id(x1))
    print("x1: ", x1)


a1 = 10
print(id(a1))
update(a1)
print("a1: ", a1)


# Example 4
def update(lst):
    print(id(lst))
    lst[1] = 40
    print(id(lst))
    print("lst: ", lst)


lst = [10, 20, 30]
print(id(lst))
update(lst)
print("lst: ", lst)
