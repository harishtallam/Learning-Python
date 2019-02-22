# syntax verification tuple and list

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]

#tuple[2] = 1000    # Invalid syntax with tuple

#before update
print ("before update:", list)
list[2] = 1000     # Valid syntax with list

#after update
print ("after update:", list)