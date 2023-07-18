#Date: 11-07-2023
#Day : Tuesday


#lamda function or anonymous function
def sample(i):
    pass
a=lambda i:i+1
print(a(5))
print(type(a))
#recrusive function
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(10))
#print the number odd or even using lambda function
#number=int(input("enter a number:"))
#odd_even=lambda:"even number"
#if number % 2 == 0 else "odd number"
#print(odd_even())

#map object
def make_sum(i):
    return i+1
#print(list(map(make_sum,range(20))))
ot=map(make_sum,range(20))
for i in ot:
    print(i)