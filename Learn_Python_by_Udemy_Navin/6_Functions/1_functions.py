# Functions - Functions are objects in Python

# defining a function
def greet():  # simple function
    print("Hello")
    print("Good Morning")


def add(x, y):  # argument based function
    z = x + y
    print(z)


def add1(x, y):  # argument based function with return
    z = x + y
    return z


def add_sub(x, y): # argument based function with multiple return statements
    z = x + y
    s = x - y
    return z, s


# calling a function
greet()

add(2, 3)

result = add1(5, 4)
print(result)

result1, result2 = add_sub(5, 4)
print(result1, result2)
