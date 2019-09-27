import os

# Open a file
#fo = open(r"D:\Installations\python-workspace\files_learn\foo.txt", "r+")
os.remove("foo.txt")
os.remove("oof.txt")
fo = open("foo.txt", "w+")

fo.write("Amazing.. \nZing Zing\n")
str = fo.read(10)
print ("Read string is:", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print ("Again read String is : ", str)
fo.close()

os.rename("foo.txt","oof.txt")


