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