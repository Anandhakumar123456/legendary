#Date: 07-07-2023
#Day : Friday



#create function 


#vowels 




def Check_Vow():
    vowels=['a','e','i','o','u']
    string=input("Enter the string:")
    string = string.casefold()
    count = {}.fromkeys(vowels, 0)
    for character in string:
        if character in count:
            count[character] += 1   
    return count


#print(Check_Vow())


#Multiplication table 

def multi():
    n=int(input("Enter the table you want:"))
    for i in range(1,11):
        print(i,"*",n,"=",n*i)
    else:
        print("Table completed..")
    return 0        

#multi()

#odd or even


def oddoreven():
    n=int(input("Enter the number: "))
    if n%2==0:
        print("This is Even number.")
    else:
        print("This is Odd Number.")
    return 0      


#oddoreven()


while True:
        print("1. Vowel Check")
        print("2. Odd or Even Number Check")
        print("3. Multiplication Table ")
        n=int(input("Choose the operation: "))
        if n==1:
            print(Check_Vow())
        elif n==2:
            oddoreven()
        elif n==3:
            multi() 
        else:
            print("Invalid Option. please Enter the valid Option")  

        option=int(input("Do You Want to Continue ( Yes for 1 / No for 0 ): "))  
        if option == 1:
            continue    #continue the loop 
        else:
            break      #exit the loop 
        



"""
        option=input("Do You Want to Continue(Y/N)")  
        if option == 'Y' or 'y':
            continue
        else:
            break"""