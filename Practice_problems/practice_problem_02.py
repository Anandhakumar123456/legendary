#Date: 19-07-2023
#Day : Wednesday 



#1) Greatest Number:

def greatest_num():
    a,b,c=10,12,50
    if a>b and a>c:
        print("A is Greatest Number. ")
    elif b>c and b>a:
        print("B is Greatest Number. ")
    else:
        print("C is Greatest Number. ")    


#2) String/Number Reverse:

def rev_str():
    str=input("Enter the String/Numbers:")
    str=str[::-1]
    return str

#b=rev_str()
#print(b)


#3) Find Temperature in Celsius:

def find_temp():
    temp=float(input("Enter the temperature in Celsius:"))
    if temp<-273.15:
        print("The temperature is invalid because it is below absolute zero.")
    elif temp==-273.15:
        print("The temperature is absolute 0.")    
    elif temp in range(float(-273.15,0)) :
        print("The temperature is below freezing.")
    elif temp==0:
        print("The temperature is at the freezing point.") 
    elif temp in range(0,100) :
        print("The temperature is in the Normal range.")        
    elif temp==100:
        print("The temperature is at the Boiling point.") 
    else:
        print("The temperature is at the above Boiling point.")  


#find_temp()


#4) Find Leap Year or Not:

def leap():
    year=int(input("Enter the year to find Leap or Not:"))
    if (year%400==0) and (year%100==0):
        print("{0} is Leap Year.".format(year))
    elif (year%4==0) and  (year%100!=0):
        print("{0} is Leap Year.".format(year))
    else:
        print("{0} is Not a Leap Year.".format(year))

#leap()

#5) List of Integers:

def find_elements():
    n=input("Enter the Numbers:")
    n=list(n)
    total=len(n)
    n.reverse()
    n2=n[1:-1]
    n2.sort(reverse=False)

    #print(n)
    print("Total Number of elements:",total)
    print("Last item of the list :",n[-1])
    print("Reverse Oredr of the list :",n)
    if n is '5':
        print("Yes")
    else:
        print("No")  
    print("Remaining items of the list is : " ,n2)


#find_elements()


#6) List operations.

mylist=[8,9,10]
print(mylist[2]) #10

mylist[1]=17
print(mylist) #set the value 17 at the second index.

#Adding the elements 4,5,6 in the list.
mylist.append(4)
mylist.append(5)
mylist.append(6)
print(mylist)  #[8, 17, 10, 4, 5, 6]

#Removing the first element in the list.
mylist.remove(mylist[0])
print(mylist)  #[17, 10, 4, 5, 6]

#Sorting the list.
mylist.sort()
print(mylist) #[4, 5, 6, 10, 17]

#Inserting the value 25 in the 3rd index.
mylist[3]=25
print(mylist) #[4, 5, 6, 25, 17]

mylist.extend(mylist)
print(mylist) #10 is missing.


# 7) Dictionary Operations:

mydict={'Anandhakumar': '12345', 'Babu': 'babu', 'Saran': 'saran123', 'Ganesh': 'ganesh123', 'Ram': 'ram123', 'Ammu': 'ammu123', 'Bala': 'bala123', 'Suresh': 'suresh123', 'Sam': 'sam123', 'Tom': 'tom123', 'Gokul': 'gokul123'}

print(mydict)


for username,password in mydict.items():
    username=input("Enter the Username:")
    password=input("Enter the Password:")
    if username not in mydict.keys():  
        print("The username is not valid for the system.")
    elif username in mydict.keys() and password not in mydict.values():
        print("The password is invalid.") 
    else:
        print("You are Logged in the system.")  
        break
