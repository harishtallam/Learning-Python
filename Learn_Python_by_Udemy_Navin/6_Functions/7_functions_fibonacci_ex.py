# Example 1
# Simple example
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c

        print(c)


fib(5)

print()


# Example 2
# with if condition to control the hardcoded values in result
def fib1(n):
    a = 0
    b = 1
    # The reason "if" condition is added is that if the input is 1, it should print only 1 value which
    # already hardcoded in "a" variable. And this is not handled in ex-1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c

            print(c)


fib1(1)
fib1(2)

print()


# Example 3
def fib2(n):
    a = 0
    b = 1
    # The reason "if" condition is added is that if the input is 1, it should print only 1 value which
    # already hardcoded in "a" variable. And this is not handled in ex-1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            # prints only fib till 100 value
            if c <= 100:
                print(c)


fib2(20)
fib2(110)
print()


# Example 4
def fib3(n):
    # Checks whether given value is negative or not
    if n < 0:
        print("Invalid Number")
    else:
        pass
    a = 0
    b = 1
    # The reason "if" condition is added is that if the input is 1, it should print only 1 value which
    # already hardcoded in "a" variable. And this is not handled in ex-1
    if n > 0:
        pass
        if n == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c = a + b
                a = b
                b = c
                # prints only fib till 100 value
                if c <= 100:
                    print(c)


fib3(-2)
fib3(100)
fib3(int(input("Enter the number: ")))
