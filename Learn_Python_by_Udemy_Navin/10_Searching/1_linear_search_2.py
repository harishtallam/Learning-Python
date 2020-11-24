# Example 1

# As the list starts with index 0, this is given as "-1"
pos = -1


def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1

    return False


# This is list
list = [2, 5, 9, 13, 18]

# This is what we need to search
n = 9


if search(list, n):
    print("Found the number at: ", pos)  # pos+1 to understand the position in human way
else:
    print("Number not found")