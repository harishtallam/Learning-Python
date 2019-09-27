# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")



# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)



# Function definition is here
def changeme1( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4] # This would assig new reference in mylist    
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme1( mylist )
print ("Values outside the function: ", mylist)


# Function definition is here
def printme1( str ):
   "This prints a passed string into this function"
   print (str)
   return
# Now you can call printme function
printme1( str = "My string")


# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return
# Now you can call printinfo function
printinfo( age=50, name="miki" )



# Function definition is here
def printinfo1( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return
# Now you can call printinfo function
printinfo1( age=50, name="miki" )
printinfo1( name="miki" )



# Function definition is here
def printinfo2( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
# Now you can call printinfo function
printinfo2( 10 )
printinfo2( 70, 60, 50 )


# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2
# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))



# Function definition is here
def sum1( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total
# Now you can call sum function
total = sum1( 10, 20 )
print ("Outside the function : ", total)


total = 0 # This is global variable.
# Function definition is here
def sum2( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2 # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total
# Now you can call sum function
sum2( 10, 20 )
print ("Outside the function global total : ", total)

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   # global Money
   #Money = Money + 1
   print (Money)
AddMoney()
print (Money)