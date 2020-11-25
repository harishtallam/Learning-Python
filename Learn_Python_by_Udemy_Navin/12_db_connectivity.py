# Ensure mysql-connector module is installed

import mysql.connector

# Example 1
mydb = mysql.connector.connect(host="localhost", user="harish", passwd="12345")
mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)


# Example 2
mydb = mysql.connector.connect(host="localhost", user="harish", passwd="12345", database="my_database")

mycursor.execute("select * from table_name")
for i in mycursor:
    print(i)

# Example 3
result = mycursor.fetchall()
for i in result:
    print(i)


# Example 4
result = mycursor.fetchone()
print(result)
for i in result:
    print(i)