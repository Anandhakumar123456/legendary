
#Date: 20-06-2023
#Day : Tuesday


#----------------------Topic: How a variable works---------------------

# id() function's scope and work

#id() function is represent the memory address of the variable.

a=1
a=2 #same memory address "X1000"

print(id(a),"\n")

# if memory was already allocated in a particular value  ( a=2 ), it won't create a momory for same value of variable ( b = 2 , c = 2 ). bcz it will use it.

c=2 #same memory address "X1000" 
b=2 #same memory address "X1000"
c=1

print(id(b),"\n")

print(id(c),"\n")
d=4
print(id(d),"\n")
