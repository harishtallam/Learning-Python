# Example 1

def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            return True
        i = i + 1

    return False


# This is list
list = [2, 5, 9, 13, 18]

# This is what we need to search
n = 20


if search(list, n):
    print("Found the number")
else:
    print("Number not found")