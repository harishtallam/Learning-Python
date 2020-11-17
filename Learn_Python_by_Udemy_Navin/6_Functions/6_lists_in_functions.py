# Pass List to a function
# Count number of even and odd numbers in a list

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


lst = [1, 3, 5, 8, 10, 13, 18]

even, odd = count(lst)

print(even, odd)

print("Even: {} and Odd: {}".format(even, odd))
print(f'Even: {even}, Odd: {odd}')

"""
Assignment
1. Take 10 names from the user, and display the names which length is more than 5
"""
# Sol: 1

arr = []
n = 10
for i in range(n):
    x = input("enter the name: ")
    arr.append(x)
print(arr)
# Count and display the names with length more than 5
cnt = 0
for j in arr:
    if len(j) > 5:
        print("name:{},length:{}".format(j, len(j)))
        cnt += 1
print("Total number of names with length more than 5 is:", cnt)

# Sol 2:
more = []
less = []
lst = []


def count(lst):
    for i in lst:
        if len(i) >= 5:
            more.append(i)
        else:
            less.append(i)
    return more, less


x = int(input("Enter the limit: "))

for i in range(x):
    lst.append(input("Enter the name: "))

more, less = count(lst)
print("Names with more than 5 characters", more, "\n")
print("Names with less than 5 characters", less)


# Sol: 3
def names(user):
    count1 = 0
    for j in user:
        if len(j) > 5:
            count1 += 1

    return count1


x = int(input('enter the total number of names'))
lst = []
for i in range(x):
    x = input('enter the names')
    lst.append(x)
print(lst)
count1 = names(lst)
print('names greater than length five are: {}'.format(count1))


# Sol 4:
def count2(lst1):
    e = 0
    r = 0
    for k in lst1:
        if len(k) > 5:
            e += 1
        else:
            r += 1
    return e, r


lst1 = ['venkata', 'harish', 'tallam', 'bbc', 'gnt']
extra, right = count2(lst1)
print("Name greater than length 5 are: {} and Name less than 5 are: {}".format(extra, right))
