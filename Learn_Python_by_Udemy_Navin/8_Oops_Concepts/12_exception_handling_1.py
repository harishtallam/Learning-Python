a = 5
b = 0

# Example 1
try:
    print(a/b)
except Exception:
    print("A number cannot be divided by zero")

# Example 2
try:
    print(a/b)
except Exception as e:
    print("A number cannot be divided by zero:", e)

# Example 3
a = 5
b = 2
try:
    print(a/b)
    k = int(input("Enter the value: "))
except Exception as e:
    print("A number cannot be divided by zero:", e)

# Example 4
a = 5
b = 2
try:
    print(a/b)
    k = int(input("Enter the value: "))
except ZeroDivisionError as e:
    print("A number cannot be divided by zero:", e)
except ValueError as e:
    print("Invalid input", e)
except Exception as e:
    print("Something went wrong:", e)

# Example 5
a = 5
b = 2
try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter the value: "))
except ZeroDivisionError as e:
    print("A number cannot be divided by zero:", e)
except ValueError as e:
    print("Invalid input", e)
except Exception as e:
    print("Something went wrong:", e)
finally:
    print("Resource closed")
