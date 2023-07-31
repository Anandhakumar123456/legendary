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
    elif -273.15<= temp < 0 :
        print("The temperature is below freezing.")
    elif temp==0:
        print("The temperature is at the freezing point.") 
    elif 0 <=temp < 100:
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

def pass_check():

    mydict={'Anandhakumar': '12345', 'Babu': 'babu', 'Saran': 'saran123', 'Ganesh': 'ganesh123', 'Ram': 'ram123', 'Ammu': 'ammu123', 'Bala': 'bala123', 'Suresh': 'suresh123', 'Sam': 'sam123', 'Tom': 'tom123', 'Gokul': 'gokul123'}

#print(mydict)

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


#pass_check()

#8) Rotates the elements in the list.

lst=[2,6,3,8,4]


def rotate_list(lst):
    if not lst:  # not means empty list
        return lst
    last_item=lst[-1]
    for i in range(len(lst)-1,0,-1):
        lst[i]=lst[i-1]   #lst[4]=lst[4-1]
    lst[0]=last_item
    return lst    

rotated_list=rotate_list(lst)

#print(rotated_list)



#9) Count donuts:

def donuts(count):
    if count>=10:
        return "Number of donuts  : 'many' "
    else:
        return "Number of donuts  :{}".format(count)
    

#print(donuts(1)) 

#10) Return 2 character of string:


def first_and_last2char(s):
    if len(s)==2:
        return(s)
    else:    
        return(s[0:2]+s[-2:])

#print(first_and_last2char("sp"))



#11) Check the same strings first and last characters:

strings=['deed','hello','world','mam','pop','sos','laptop','did']
def same_end_strings():
    count=0
    for i in strings:
        if len(i)>=2 and i[0]==i[-1]:
            count+=1  # if above the conditions are true the count variable incremented by one. 
    return(count)        

#x=same_end_strings()
#print(x)


#12) Multiples of 3 or 5 below 1000:

def sum_multiple_3_5(limit):
    sum_of_num=0
    for i in range(limit):
        if i%3==0 or i%5==0:
            sum_of_num+=i
    return sum_of_num

#print(sum_multiple_3_5(100))


#13) Fibonacci Series:


def fibonacci_sum_even(limit):
    prev_num = 1
    current_num = 2
    even_sum = 0

    while current_num <= limit:
        if current_num % 2 == 0:  
            even_sum += current_num

        next_num = prev_num + current_num
        prev_num = current_num
        current_num = next_num

    return even_sum

#print(fibonacci_sum_even(4000000))



#14) Remove duplicates in array:

array=[1,2,3,4,5,6,5,4,3,2,1]

def remove_duplicates(array):
    return list(set(array)) #Bcz set is not allow duplicate items 

#print(remove_duplicates(array))


#15) Random code generator :

import random

def random_with_no_range(min_value,max_value):
    return random.randint(min_value,max_value)

#print(random_with_no_range(1,90))

#16) Prime Numbers:

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_of_primes_below(limit):
    prime_sum = 0
    for number in range(2, limit):
        if is_prime(number):
            prime_sum += number
    return prime_sum


#17) Not present in the array:

array1=[1,2,3,4,5]
array2=[2,3,1,0,5]

def miss_number(arr1,arr2):
    for i in arr1:
        if i not in arr2:
            return f"The missing Number is :{i}"

#print(miss_number(array1,array2))


#18) Sum of squres:

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))  # 100+81+64+49+36+25+16+9+4+1  =385

def square_of_sum(n): # 10+9+8+7+6+5+4+3+2+1 =55 **2 = 3025
    return sum(range(1, n+1))**2  #sum( range(1, 11 ))**2


limit = 100

# Calculate the sum of the squares of the first one hundred natural numbers

sum_of_squares_result = sum_of_squares(limit)

# Calculate the square of the sum of the first one hundred natural numbers

square_of_sum_result = square_of_sum(limit)

# Find the difference

difference = square_of_sum_result - sum_of_squares_result

#print(f"The difference is: {difference}")

#19) Area and perimeter of the circle:

def area_and_perimeter():
    pi=3.14
    r=3
    print("Area of the circle is :"+pi*r*r)
    print("Perimeter of the circle is :"+2*pi*r)

#20) Greetings:

greeting = "Hello Google!"

number_of_characters=len(greeting)

repeated_greeting=number_of_characters*greeting
print("Repeated greetings: ",repeated_greeting)


#21) reads an integer N (1 < N < 1000):

def generate_output(N):
    for i in range(1,N+1):
        print(f"{i} {i*2} {i**3}")

N=int(input("Enter the limit: "))

if N<1000:
    print(generate_output(N))
else:
    print("Invalid Number. N Should be 1 to 999.")    


#22) Password validation:
"""import re
def password_validation(password):
    if len(password)<=6 :
        print("Password must be above 6-8 characters.")
    else:
        re.match("r^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$",password)
        
password=input("Enter the password for validation:")

passwords_sample=["abc123", "Passw0rd", "qwerty", "Abc1234", "myp@ss"]

for i in passwords_sample:
    if password_validation(i):
        print(f"Password {password} is valid.")
    else:
        print(f"Password {password} is invalid.")   """ 

#23) Read two numbers M and N indefinitel factorial :



#24) Calculate salary:


def calculate_increase_salary(salary):
    if salary <= 400.00:
        increase_percentage = 15
    elif salary <= 800.00:
        increase_percentage = 12
    elif salary <= 1200.00:
        increase_percentage = 10
    elif salary <= 2000.00:
        increase_percentage = 7
    else:
        increase_percentage = 4
    
    increase_amount = salary * (increase_percentage / 100)
    new_salary = salary + increase_amount
    
    return new_salary, increase_amount, increase_percentage

def main():
    salary = float(input("Enter the salary:").strip())
    new_salary, increase_amount, increase_percentage = calculate_increase_salary(salary)
    
    print("Novo salario: {:.2f}".format(new_salary))
    print("Reajuste ganho: {:.2f}".format(increase_amount))
    print("Em percentual: {} %".format(increase_percentage))


main()
