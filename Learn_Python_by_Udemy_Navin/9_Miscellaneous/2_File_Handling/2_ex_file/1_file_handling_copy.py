file = open('mydata.txt', 'r')

file1 = open('newfile.txt', 'w')

# iterates and copies to new file
for f in file:
    file1.write(f)
