## Tuple is same as list, but the only difference is - List is mutable, where as Tuple is immutable

tup = (13,5,10,18,2)
print(tup)

print(tup[1])
# tup[1] = 32 # 'tuple' object does not support item assignment. As, Tuple is immutable


## Defining sets. Set is a collection of objects
s = {13,5,10,18,2}
print(s) # set will always print in random order

s1 = {133,53,103,183,23}
print(s1)

# Indexing is not supported in sets as it gives o/p randomly