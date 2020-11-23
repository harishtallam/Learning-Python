file = open('mydata.txt', 'r')
file1 = open('newfile.txt', 'w')

# writes data to the file (ensure the file is created)
file1.write("Something ")
file1.write("good gonna happen. ")

# a - indicates append to existing file
file1 = open('newfile.txt', 'a')

file1.write("Good for every one")
