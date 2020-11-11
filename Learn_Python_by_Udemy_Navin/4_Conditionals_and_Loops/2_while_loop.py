
i = 1
while i<=5:
    print("I'm Printing")
    i += 1
    # i = i + 1

#####################################
i = 5
while i>=1:
    print("I'm Printing new")
    i -= 1
    # i = i - 1

#####################################
i = 5
while i>=1:
    print("I'm Printing new1", i)
    i -= 1
    # i = i - 1

#####################################
i = 1
j = 1
while i<=1:
    print("I'm Printing new i", i)
    while j<=4:
        print("I'm Printing j", j)
        j +=1
    i += 1


#####################################
i = 1
while i<=5:
    print("Venkata Harish ", end="")
    j = 1
    while j<=4:
        print("Tallam ", end="")
        j +=1
    i += 1
    print()


#####################################
## Assignment
# Write a code to print all the values from 1 to 100 Skip the numbers which are divisible by 3 or 5
# Sol 1:
i = 1
while i<=100:
    if i % 3 == 0:
        i += 1
    elif i % 5 == 0:
        i += 1
    else:
        print("The numeber is:",i,end='')
        i += 1
        print()


# Sol 2:
i=1
while i<=100:
    if (i%3==0 or i%5==0):
        i=i+1
    else:
        print (i)
        i=i+1


# Sol 3:
i=1

while i<=100:
    if (i%3!=0 and i%5!=0):
        print(i)
        i=i+1
    else:
     i=i+1

"""
Write a code to print below pattern?
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
"""

# Sol 1:
i=1
while i<=4:
    print('# # # # #')
    i=i+1

# Sol 2:
i=1
while i<=5:
    print()
    print("#",end='')
    i=i+1
    j=1
    while j<=4:
        print("#",end='')
        j=j+1