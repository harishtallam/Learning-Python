##
num = [5,9,13,18,23]
num1 = [9,5,18,13,23]
#num
#num1
print(num)
print(num1)


##### Indexes of a list #####
###                    ###
###  0  1   2   3   4  ###
###  5  9  13  18  23  ###
### -5 -4  -3  -2  -1  ###
###                    ###
#############################
print(num[2]) 
print(num1[2])
print(num[0])

print(num[-1])
print(num[-5])

print(num[2:])

### String Lists ###
names = ['venkata', 'harish', 'tallam']
print(names)

### String & Number Lists ####
dob = ['venkata', '13', 'harish', '05', 'tallam', '1987']
print(dob)

## lets print lists of lists
print(num, names)

## Other in-built operations
num.append(55) ## 55 appends to the existing list
print(num)

num.insert(5,10) ## inserts 10 at index 5
print(num)

num.remove(23) ## removes number 23
print(num)

num.pop(4) ## removes basis on index
print(num)

num.pop() ## removes basis on LIFO (push,pop tech as per data structures)
print(num)

del num[3:] ## removes from 3rd index
print(num)

num.extend([2,3,1,6,32]) ##adds these number from last index
print(num)

## IN-BUILD FUNCTIONS ##
print(min(num))
print(max(num))
print(sum(num))


num.sort() ## sorts in order
print(num)