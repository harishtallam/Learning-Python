import os
import time

fo = "foo.txt"
if os.path.isfile(fo):
    print ("File foo.txt is already available")
    #os.remove("foo.txt")
    os.remove("oof.txt")
    #print ("File removed:", fo)
    os.rename("foo.txt","oof.txt")
    print ("File renamed in if condition")
    #fo.close()

else:
        os.remove("oof.txt")
        fo = open("foo.txt", "w+")
        fo.write("Amazing.. \nZing Zing\n")
        #str = fo.read(10)
        #print ("Read String is:", str)
        fo.close()
        time.sleep(5)
        os.rename("foo.txt", "oof.txt")
        print ("File renamed in else condition")

