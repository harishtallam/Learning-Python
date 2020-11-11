###########################
if True:
    print("I'm Right")


###########################
if False:
    print("Am I really right?")


###########################
x = 3
r = x % 2
if r==0:
    print("Even")
print("Bye")


###########################
x = 8
r = x % 2
if r==0:
    print("Even")
print("Bye")


###########################
x = 9
r = x % 2
if r==0:
    print("Even")

if r==1:
    print("Odd")    
print("Bye")


############################
# If-else
x = 8
r = x % 2
if r==0:
    print("Even")

else:
    print("Odd")    
print("Bye")


############################
# Nested-If
x = 8
r = x % 2
if r==0:
    print("Even")
    if x>5:
        print("Great")
    else:
        print("Not Great")

else:
    print("Odd")    
print("Bye")


############################
# If-elif-else

x = 2
if (x==1):
    print("One")
elif (x==2):
    print("Two")
elif (x==3):
    print("Three")
else:
    print("Four")


x = 3
if x==1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
else:
    print("Four")


## Assignment
# Write a code to check a given number is positive or negative
x = 1
if x==-1:
    print("The number is negative")
elif x==1:
    print("The number is positive")
else:
    print("No number")

# Take three values from user and find greatest number among them
x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
z = int(input("Enter 3rd Number: "))
if((x>y) & (x>z)):
    print("x is the largest number", x)
elif(y>2):
    print("y is the largest number", y)
else:
    print("z is the largest number", z)