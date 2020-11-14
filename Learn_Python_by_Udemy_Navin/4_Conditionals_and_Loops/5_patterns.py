
"""
Print like below:
# # # # 
# # # # 
# # # # 
# # # # 
"""
for i in range(4):
    for j in range(4):
        print("# ", end='')
    print()


"""
Print like below:
#
# #
# # #
# # # #
"""
for i in range(4):
    for j in range(i):
        print("# ", end='')
    print()


for i in range(4):
    for j in range(i+1):
        print("# ", end='')
    print()


"""
Print like below:
# # # #
# # #
# #
#
"""
for i in range(4):
    for j in range(4-i):
        print("# ",end='')
    print()


"""
Print like below:
1 2 3 4
1 2 3
1 2
1
"""
for x in range(4):
    y = 1
    y = y + x
    for z in range(4-x):
        print(z, end=' ')
        z += 1
    print()    

for i in range(0,4):
	for j in range(4-i):
		j=i+1
		i=j
		print(j,end=" ")
	print()

for i in range(5):
    for j in range(i+1,5):
        print(j,end=" ")
    print()

"""
Print like below:
A P Q R
A B Q R
A B C R
A B C D
"""
str1='ABCD'
str2='PQR'
for i in range(4):
     print(str1[ : i+1 ] + str2[ i : ])