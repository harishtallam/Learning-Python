file = open('mydata.txt', 'r')

# gives encoding and other details of the file
# print(file)

# reads entire data from a file
# print(file.read())

# Usually, this reads only 1 line at a time, to print next lines - we should repeat the same print statement
print(file.readline())
# end="" - reads without newline
print(file.readline(), end="")
print(file.readline())

# to read only some characters of the data of the line
print(file.readline(8))