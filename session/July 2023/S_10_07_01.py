#Date: 10-07-2023
#Day : Monday


#functions

def make_sum(a,b):
    return a+b
print(make_sum(5,6))

#orbitary 

def make_sum(*arg,**kwargs):
    total=sum(arg)
    total=sum(kwargs.values())
    return total
print(make_sum(5,5,5,5,5))
#
a=1
b=3
print(a if a>b else b)
c=6
print(a if (a>b) and (a>c )else b if (b>a) and (b>c)else c)

#list comprehension


print([i for i in range(1,11) if i%2==0])
print([f"(i) - even"if i%2==0 else f"(i) - odd " for i in range (1,11)])
