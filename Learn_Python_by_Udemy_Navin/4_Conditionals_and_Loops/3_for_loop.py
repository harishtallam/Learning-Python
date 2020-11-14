# Print list one after other
mylist = ['venkata', '13', 'harish', 'may', 'tallam', '1987']
for i in mylist:
    print(i)

##############################
# Print character one after other
myname='harish'
for n in myname:
    print(n)

##############################
# Print list one after other
for inlist in [13,'may',1987]:
    print(inlist)

##############################
# Print number range till 10
for num in range(10):
    print(num)

# Print number range from 11 to 21 with a gap of 2
for num1 in range(11,21,2):
    print(num1)

# Print number range from back with a gap of 1
for num2 in range(20,10,-1):
    print(num2)

##############################
# Print number range from 1 to 21 which are not divisible by 5
for num3 in range(1,21):
    if(num3%5!=0):
        print(num3)

##############################

## Assignment
# Print all the perfect square number between 1 and 500
import math
for psqr in range(500):
    x = math.sqrt(psqr)
    if int(x) ** 2 == psqr:
        print(psqr)