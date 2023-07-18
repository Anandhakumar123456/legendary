#Date: 05-07-2023
#Day : Wednesday


#Loops

#1) for in else   //else block runs if for block true or false.
#2) while

for i in range(10):
    print("Hello")

#print(("hello")*5)   

#find odd or even numbers


for i in range(1,11):
    if i%2==0:
        print(f"{i}-Even")
    else:
        print(f"{i}-Odd")
else:
    print(" for Loop completed")        


#while loop
n=10
i=1
while i<=n:
        if i%2==0:
            print(f"{i}-Even")
        else:
            print(f"{i}-Odd")
        i+=1    
else:
    print("while Loop completed")  
