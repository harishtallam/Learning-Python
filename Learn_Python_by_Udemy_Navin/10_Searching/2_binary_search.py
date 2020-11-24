pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1


list = [2, 5, 9, 10, 13, 14, 18, 23, 32, 36, 98, 123, 500, 1001, 10010, 12801]
n = 12801


if search(list, n):
    print("Found at: ", pos)
else:
    print("Not Found")
