
# rb - indicates reads binary data from a file
file = open('IMAGE_1.png', 'rb')

# wb - indicates write binary data to a file
file1 = open('IMAGE_2.png', 'wb')

for i in file:
    print(i)
    file1.write(i)


