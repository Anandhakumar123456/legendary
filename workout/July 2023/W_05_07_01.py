#Date: 05-07-2023
#Day : Wednesday



#1) find vowels in user given string.  "apple"  ['a','e']
#2) find count the characters and store the values in dictionary. "aapplleee" o/p {'a':2,'e':3}
#3) to program multipication table using while loops. i=1,n=10  total iteration is 10.
#4) iterate with strings your example in while and for loops.





#1) find vowels in user given string.  "apple"  ['a','e']

print("------------Find vowels----------------")



string=input("Enter string:")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)


#1) Finding vowels
string=input("Enter string:")
vow=['a','e','i','o','u']

def Check_Vow(string, vowels):
    string = string.casefold()
    count = {}.fromkeys(vowels, 0)
    for character in string:
        if character in count:
            count[character] += 1   
    return count


print(Check_Vow(string,vow))
#check the vowels user given the value:



#2) find count the characters and store the values in dictionary. "aapplleee" o/p {'a':2,'e':3}



#3) to program multipication table using while loops. i=1,n=10  total iteration is 10.



n=int(input("Enter the value for multipication table: \n"))

print( f"-------------------Multiplication Table {n} -----------------\n")


i=1
while i<11:
    print(f"{i} * " + f"{n} "+" = "+f"{i*n}")
    i=i+1
else:
    print("Completed..")


#Multiplication table using for loop.

"""for i in range(1,11):
    print(f"{i} * " + f"{n} "+" = "+f"{i*n}")
else:
    print("Completed..")"""

