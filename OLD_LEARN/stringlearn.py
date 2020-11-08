str = 'Hello World!'

print (str)          # Prints complete string
print (str[0] )      # Prints first character of the string
print (str[2:5])   # Prints characters starting from 3rd to 5th
print (str[2:])   # Prints string starting from 3rd character
print (str * 2)    # Prints string two times
print (str + "TEST") # Prints concatenated string


print ("My name is %s and weight is %d kg!" % ('Zara', 21))


'''
%c	character
%s	string conversion via str() prior to formatting
%i	signed decimal integer
%d	signed decimal integer
%u	unsigned decimal integer
%o	octal integer
%x	hexadecimal integer (lowercase letters)
%X	hexadecimal integer (UPPERcase letters)
%e	exponential notation (with lowercase 'e')
%E	exponential notation (with UPPERcase 'E')
%f	floating point real number
%g	the shorter of %f and %e
%G	the shorter of %f and %E
'''

# Raw Strings

print ('C:\\nowhere')
print (r'C:\\nowhere')

# Unicode Strings
# Normal strings in Python are stored internally as 8-bit ASCII, 
# while Unicode strings are stored as 16-bit Unicode. This allows for a more varied set of characters, including special characters from most languages in the world
print ('Hello, World!')
print (u'Hello, world!')


var = 'haashritha'
print("Capitalize:", var.capitalize())

str = "this is string example....wow!!!"
print ("str.center(40, 'a') : ", str.center(40, 'a'))
sub = 'i'
print(str.count(sub, 4, 40))
sub = 'wow'
print(str.count(sub))

print("Encoding:",str.encode(encoding='UTF-8',errors='strict'))
str = str.encode(encoding='UTF-8', errors='strict')
print("Decoding:",str.decode(encoding='UTF-8',errors='strict'))

#str = str.encode(encoding='base64', errors='strict')
#print("Decoding:",str.decode(encoding='base64',errors='strict'))



str = "this is string example....wow!!!"

suffix = "wow!!!"
print (str.endswith(suffix))
print (str.endswith(suffix,20))

suffix = "is"
print (str.endswith(suffix, 2, 4))
print (str.endswith(suffix, 2, 6))


print ('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2
print ("Value of x , y : ", x,y)