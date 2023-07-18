
#Date: 27-06-2023
#Day : Tuesday


#list

#1) Defining empty list
l=[]

#2) Using constructor function

list()

#3) Can convert string to list using constructor function
print(list("apple"))


#4) Passing value inside the list
l.append("apple")
l.append(123)
l.append([1,2,3])
print(l)



#5) Remove value from a list
l.remove("apple")
print(l)

#6) To check the type of a variable value
print(type(l))


#7) List is mutable  // that means change the value.
#8) List is ordered.


#8) Indexing,Slicing,Skip

l=["apple",[12,3,5],1234]
print(l[1])       #[12,3,5]
print(l[2])       #1234
print(l[1][1])    #3
print(l[0][3])    #l



#------------------------------------------


# Tuple Data type
#1) Empty tuple
t=()

#2) Tuple is immutable
#3) type check
print(type(t))



#4) tuple() -constructor function
t=tuple()

#5) if change the value in tuple, first convert the tuple to list, after change the value in it.
# T - L - O - T       T-tuple,   L- list  , O- operation  That means insert or remove, T- again convert to tuple

t=list(t)
print(t)
t.append("apple")
t.append(1)
t.append(2)
t.append(3)
print(t)
t=tuple(t)
print(t)

#6) Indexing,Slicing,Skip

print(t)   #('apple',1,2,3)
print(t[2])  # 2
print(t[0::2])  #('apple', 2)