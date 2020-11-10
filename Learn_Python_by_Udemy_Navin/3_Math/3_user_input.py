x = input("Enter 1st Number: ")
a = int(x)
y = input("Enter 2nd Number: ")
b = int(y)
z = a + b
print(z)

##########################################

m = int(input("Enter 1st Number: "))
n = int(input("Enter 2nd Number: "))
p = m + n
print(p)

##########################################

ch = input("Enter a character: ")
print(ch[0]) # As python does not have char data type, we can use indexing to print a character of an input
print(ch) # This gives an entire string which is provided as input

##########################################

ch1 = input("Enter a character: ")[0] # Considers only 1st index
print(ch1)

##########################################

result = eval(input("Enter an expression: "))
print(result)