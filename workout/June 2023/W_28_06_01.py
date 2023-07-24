#Date: 28-06-2023
#Day : Wednesday



#---------------set data type and its function------------#

# check set's inbuilt function:

print(dir(set))

#1) add() -- adds an element to the set:

fruits = {"apple", "banana", "cherry"}

print(fruits)    #output is {'banana', 'apple', 'cherry'}

fruits.add("orange")

print(fruits)    #output is {'apple', 'banana', 'orange', 'cherry'}


#2) clear() --  removes the all elements:

#fruits.clear()
print(fruits)   # output is set()

#3) copy() -- returns a copy of the set:

fruits = {"apple", "banana", "cherry"}
cpy_set=fruits.copy()

print(cpy_set)      #output is {'cherry', 'banana', 'apple'}   //it returns reverse of the set.


#4) difference() -- it returns the contains the items only 1st set.

fruits = {"pine", "banana", "cherry"}
fruits1 = {"apple", "mango", "pine"}

op=fruits.difference(fruits1)

print(op)     #output is {'cherry', 'banana'}


#5) difference_update() -- removes the items that exist in both sets.

fruits = {"pine", "banana", "cherry"}
fruits1 = {"apple", "mango", "pine"}

op=fruits.difference_update(fruits1)

print(fruits)   #output is {'banana', 'cherry'} 


#6) discard() -- remove the specified item.

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")    #removes only banana

print(fruits)   #output is {'apple', 'cherry'}



#7) intersection() -- it returns same elements in one or more sets.

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result=x.intersection(y,z)

print(result)     #output is {'c'}  bcz 'c' is in all the sets.

#8) intersection_update() -- removes the items or elements not present in both sets or all sets.

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result1=x.intersection_update(y,z)

print(x)     #output is {'c'}  bcz it removes all the not presented elements in the all sets.     //step 1 :returns the intersection      //step 2: removes the all element except the returned value.

#9) isdisjoint() -- returns True none of the elements are present in both sets, otherwise it returs False.

#Method 1:

x={"apple","orange","banana"}
y={"bikes","cars","laptops","mobiles"} 
z=x.isdisjoint(y)

print(z)   #output is True.bcz no elements matches.

#Method 2:

a={"apple","orange","mango"}
b={"pine","apple","grapes"}
c=a.isdisjoint(b)
print(c)     #output is False. bcz "apple" matches in the two sets.

#10) issubset() -- returns True if all items in the set exists in the specified set, otherwise it returns False.


m={"d","e","f"}                 #it is subset.
n={"a","b","c","d","e","f"}     #it is superset.
o=m.issubset(n)
print(o)     #output is True. bcz all items in the set.


#11) issuperset() -- returns True if all items in the specified set exists in the original set, otherwise it returns False.



#What is superset?    
#   The super set is bigset.

x = {"f", "e", "d", "c", "b", "a"}   #it is superset.
y = {"a", "b", "c"}                  #it is subset.

z = x.issuperset(y)

print(z)       #output is True. bcz all items in the set.


#12) pop() -- removes the random item from the set 
#Note  : This method is returns only removed items.

x = {"f", "e", "d", "c", "b", "a"}

res=x.pop()
print(res)      #output is "element".  bcz it was removed from the set.

print(x)        #output is removed element.

#13) remove() -- removes the specified element of the set.

a={'apple','orange','mango','banana'}
a.remove('banana')
print(a)    #output is {'orange', 'mango', 'apple'}

#14) symmetric_difference() -- it returns a set that contains all items from both sets, edcept items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)         #output is {'banana', 'microsoft', 'google', 'cherry'}  //bcz "apple" is present in both sets. so, it will excepts and prints all remaining items.



#15) symmetric_difference_update() -- opposite of symmetric_difference() method.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)        #output is {'microsoft', 'cherry', 'banana', 'google'}


#16) union() -- returns a set that contains all items from both sets, duplicates are excluded or skipped.

x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.union(y)

print(z)      #output is {'google', 'microsoft', 'cherry', 'apple', 'banana'}   //one "apple" was skipped. bcz it is duplicated.


#17) update() -- it updates the current set, by adding the another set.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y) 
print(x)     #output is {'apple', 'google', 'cherry', 'microsoft', 'banana'}.




#------------Dictionary Datatype-----------------------#



print("------------------------------------\n")
print("-----------Dictionary data type--------\n")

#1) clear() -- removes all the elements from the dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#car.clear()         #removes all the elements from the dictionary.

print(car)       #output is {}


#2) copy() -- it returns the copy of the specified dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.copy()

print(car)   #output is {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(x)     #output is {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#3) fromkeys() -- returns a dictionary with the specified keys and the specified value.

#Method 1:

x={'k1','k2','k3'}
y=1        # All key's values are 1
z=dict.fromkeys(x,y)

print(z)        # output is  {'k1': 1, 'k3': 1, 'k2': 1}


#4) get() -- returns the value of the item with the spcified key.


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

z=car.get("brand")

print(z)        #output is Ford.



#5) pop() -- removes the specified item from the dictionary.   / it removes both key and their value.  "key":"value".


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.pop("model")

print(car)      #output is {'brand': 'Ford', 'year': 1964}


#6) popitem() -- it removes the last inserted items from the dictionary.   // it removed item returns as a tuple. ()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964        #this is last inserted item 
}

x=car.popitem()
print(x)        #output is ('year', 1964)


#7) setdefault() -- returns the value of the item with the specified key.if the key doesn't exist, insert the  key first and get the value.


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.setdefault("color", "white")

print(x)         #output is white


#8) update() -- inserts the values to the dictionary.


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.update({"color":"white"})        #using curly brackets{ }.

print(car)      #output is  {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}


#9) values() -- it returns readable format. it returns only values.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x=car.values()

print(x)        #output is dict_values(['Ford', 'Mustang', 1964])



