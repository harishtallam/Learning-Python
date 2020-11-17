# Factorial of a number
# Eg: Factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120
def fac(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


x = 5

result = fac(x)
print(result)