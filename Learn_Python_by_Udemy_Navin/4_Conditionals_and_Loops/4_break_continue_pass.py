##### Continue example 0
# Print numbers till you reach 3 in a range of 5
for i in range(5):
    if i==3:
        break
    print("Hello", i)

##### Break example 1
# Assume you have 5 candies and user is requesting more than 5
available = 5
req = int(input("How many candies? "))

i = 1
while i <= req:
    if i > available:
        print ("Out Of Stock")
        break

    print("Candy")
    i += 1
print("Candies available are 5")

##### Continue example 0
# Print numbers which are not equal to 3
for i in range(5):
    if i==3:
        continue
    print("Hello", i)

##### Continue example 1
# Print only which are not divisible by 3 
for i in range(1,101):
    if i%3==0:
        continue
    print(i)

print("Bye")

##### Continue example 2
# Print only which are not divisible by 3 or 5
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

print("Bye")

##### Pass example 1
# Print only even numbers
for i in range(1,101):
    
    if (i%2!=0): 
        pass
    else:
        print(i)
print("Bye")


########################################
## Assignment 1
# Print first fibonacci numbers
## Sol: 1 --> Check this again
x,y=0,1
i=0
while i<50:
    print(y,' ')
    x,y = y,x+y
    i+=1
print('BYE')

## Sol: 2
list1 = [0, 1]
for i in range(48):
    list1.append(list1[-1]+list1[-2])
print('bye')
print(list1)

## Sol: 3
a=0
b=1
print(a)
print(b)
for i in range(0,48):
 c=a+b
 print(c)
 a=b
 b=c

## Assignment 2
# Check a given number is prime or not
x = int(input("Enter a number: "))
i = 2
while i <= x:
    if x % i == 0:
        if x != i:
            print(x, "is Not a Prime number")
            break
        else:
            print(x, "is a Prime Number")
    i = i+1
print("Thank You")