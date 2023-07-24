#Date: 19-07-2023
#Day : Wednesday 



def star_pattern1():
    print("\n 1) Star pattern.")
    n=int(input("Enter the Number for print the star pattern:\n"))
    for i in range(n+1):
        print("* "*i)

def star_pattern_rev2():
    print("\n 2) Star pattern (Decrement):")
    n=int(input("Enter the Number for print the star pattern:\n"))
    for i in range(n,0,-1):
        print("* "*i)    



def star_pattern_space3():
    print("\n 3) Star pattern with space :")
    n=int(input("Enter the Number for print the star pattern:\n"))
    for i in range(n+1):
        print('  '*(n-i)+'* '*i)        


def star_pattern_space_dec4():
    print("\n 4) Star pattern (Decrement):")
    n=int(input("Enter the Number for print the star pattern:\n"))
    for i in range(n,0,-1):
        print('  '*(n-i)+"* "*i) 



def check_vow5():
    vowels=['a','e','i','o','u']
    string=input("Enter the string: ") #Apple
    string=string.casefold()
    count={}.fromkeys(vowels,0)

    for characters in string:
        if characters in count:
            count[characters]+=1
    return count    
