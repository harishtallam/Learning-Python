# Open a file
fo = open(r"D:\Installations\python-workspace\files_learn\foo.txt", "wb")
print ("Name of the file:", fo.name)
print ("Closed or Not:", fo.closed)
print ("Opening Mode:", fo.mode)
#print ("Softspace Flag:", fo.softspace)
fo.close()
print ("Closed or Not:", fo.closed)
