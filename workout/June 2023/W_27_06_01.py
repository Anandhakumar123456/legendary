#Date: 27-06-2023
#Day : Tuesday


# -------------------List inbuilt functions-----------------------------#
l=[]


#1) append()--   add an element inside the list

l.append("apple")  #add only one element at once.
l.append("orange")  
l.append("banana")  
l.append("pine") 

print(l)  #output ['apple','orange','banana','pine']



#2) clear() --  remove all the elements from the list

#l.clear()

print(l)     # output []


#3) copy() -- it helps copy of the list

l_2=l.copy()
print(l_2)   #output ['apple','orange','banana','pine']


#4) count() -- it returns total elements with specified value in the list

l_2=l_2.count("apple")   
print(l_2)      #output is 1 bcz "apple" is one time accurs.


#5) extend() -- add the elements of the list at the end.

bikes=['R15','MT15','Kawasaki Ninja','BMW S100RR']

cars=['Audi','Ferrari','Tesla','RR']

bikes.extend(cars)
print(bikes)    # output  ['R15', 'MT15', 'Kawasaki Ninja', 'BMW S100RR', 'Audi', 'Ferrari', 'Tesla', 'RR']


#6) index() --  it returns the position of the first accurance of the specified value.

print(bikes)

pos=bikes.index("Ferrari")   #it returns the ferrari's index position.         
print(pos)        # output is 5


#7) insert() --  add an element at the user specified index position.

print(bikes)
bikes.insert(4,"KTM")

print(bikes)    #output is ['R15', 'MT15', 'Kawasaki Ninja', 'BMW S100RR', 'KTM  => inserted value  ', 'Audi', 'Ferrari', 'Tesla', 'RR']

#8) pop() -- removes an element at the specified postion.

print(bikes)

bikes.pop(1)  #removes the 'MT15' in the list

print(bikes)   #output is ['R15','Kawasaki Ninja', 'BMW S100RR', 'KTM', 'Audi', 'Ferrari','Tesla', 'RR']

#9) remove() -- removes the particular element in a spcified value.

bikes.remove("KTM")
print(bikes)   #output is ['R15', 'Kawasaki Ninja', 'BMW S100RR', 'Audi', 'Ferrari', 'Tesla', 'RR']


#10) reverse() -- reverse the order of the list.

bikes.reverse()

print(bikes)  #output is ['RR', 'Tesla', 'Ferrari', 'Audi', 'BMW S100RR', 'Kawasaki Ninja', 'R15']

#11 sort() -- sort the list by ascending or decending order.

# *) Ascending order:

numbers=[1,2,3,4,5,6,7,8,9]
numbers.sort()
print(numbers)


# *) Descending order:

numbers=[1,2,3,4,5,6,7,8,9]
numbers.sort(reverse=True)
print(numbers)


#-------------Tuple data type and its function ---------------------#





print("-----------------------------")
print("-------------Tuple----------------")

#1) count() -- it returns the number of times accurs a specified value in a tuple.

#Method 1:

tuple1=(1,2,3,4,5,6,7,8,9,2,1,5,5,2,2,0,2,2)
print(tuple1.count(2))   #output is 6   bcz "2" is 6 times accurs.


#Method 2:

ans=tuple1.count(5)
print(ans)      #output is 3  bcz 5 is 3 times accurs.

#2) index() --  it searches and returns a postion of the  specified value.

print(tuple1)
print(tuple1.index(2))   #output is 1 "2" is placed in 1st position of the tuple. 

#Note: It returns first accurance only.


