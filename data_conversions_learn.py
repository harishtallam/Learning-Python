a = 10.0
float(a)
print("float a:", a) # Converts x to a floating-point number

b = "Hi Harish"
str(b)
print("string b:", b) # Converts object x to a string representation

c = 10*20
repr(c)
print("Expression c:", c) # Converts object x to an expression string

d = "Hi Harish"
eval("d")
print("Evaluation of String d:", d) # Evaluates a string and returns an object

e = "10"
eval("e")
print("Evaluation of String d & e:", d, e) # Evaluates a string and returns an object
print("Evaluation of String d & e:", d+e) # Evaluates a string and returns an object

f = ( 'abcd', 786 , 2.23, 'john', 70.2  ) # Tuple
tuple(f)
print("Tuple:", f) # Converts to a tuple

g = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
list(g)
print("List:", g) # Converts to a list.

s = set(["a", "b", "c"]) # This is normal set. A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements
print("Normal Set:", s)
s.add("d")
print("Normal Set after addition:", s)

t = frozenset(["a", "b", "c"]) # This is frozen set where we cannot add more more elements in it
print("Frozen Set:", t) 

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
#Creates a dictionary. d must be a sequence of (key,value) tuples.
print (dict['one'])      # Prints value for 'one' key
print (dict[2])          # Prints value for 2 key
print (tinydict)        # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

u = int (2000) 
u1 = chr(u)
print("Character:", u1) # Conversion of Integer to a character

v = int (2000) 
v1 = chr(v)
print("Unicode Character:", v1) # Conversion of Integer to a Unicode character

w = chr(100)
w1 = ord(w)
print("Integer value:", w1) # Converts a single character to its integer value

x = int (2000)
x1 = hex(x)
print("Hexadecimal String:", x1) # Converts an integer to a hexadecimal string

y = int (2000)
y1 = oct(y)
print("Octal String:", y1) # Converts an integer to an octal string

xx = "-100"
int(xx, base=10) # Converts x to an integer. base specifies the base if x is a string
print(xx)

yy = "10"
int(yy,base=10)
yy.__init__()

zz = -10
int(zz)
print (zz)

xxx = -100
yyy = "-100"
#float(xxx, base=10)
float(xxx) # Converts x to an integer. base specifies the base if x is a string
print(xxx)
float(yyy)
print(yyy)