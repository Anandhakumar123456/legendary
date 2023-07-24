#Date: 04-07-2023
#Day : Tuesday


#conditional statements:

#if:
#if-else:
#elif:
#nested if:

#This is if statement:
a=5
b=3

if a>b:
    print("a is greater number.")
else:
    print("b is greater number.")  

#This is if else statement:

a=1 #
b=3

if a>b:
    print("a is greater number.")
else:
    print("b is greater number.")    

print("---------------------")
#elif statement:

a=1
b=4
c=5
a=0
b=0
c=0
if(a>b) and (a>c):
    print("a is greater number.")
elif(b>c) and (b>a):
    print("b is greater number.")
elif(c>a) and (c>b):
    print("c is greater number.") 
else:
    print("all values are same.") 


#Nested if:
a=1
b=4
c=5

if(a>b):
    if(a>c):
        print("a is greater number.")
    else:
        if(b>c):
            print("b is greater number.") 
        else:
            print("c is greater number.")
elif(b>c) and (b>a):
    print("b is greater number.")
elif(c>a) and (c>b):
    print("c is greater number.") 
else:
    print("all values are same.") 



