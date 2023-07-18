#Date: 13-07-2023
#Day : Thursday


#LEGB Rule
#L-Local
#E-Enclosed
#G-Global
#B-Builtin
a=1



def fun1():
    global a
    b=2
    #print(f"fun1 scope a-{a}")
    print(f"fun1 scope b-{b}")
    a=4
    print(f"fun1 scope a-{a}")
    def fun2():
        global a
        nonlocal b
        c=3
        a=7
        print(f"fun2 scope a-{a}")
        
        b=5
        print(f"fun2 scope b-{b}")
        print(f"fun2 scope c-{c}")
    fun2()
    print(f"fun1 scope b- {b}")    
    #print(f"fun1 scope c- {c}")    

fun1()
print(f"global scope a -{a}")
#print(f"global scope b -{b}")



#filter
#syntax - filter(fn,iterable)
#return - filter object

#print(list(filter(lambda i:False if i%2==0 else True,range(1,11))))  #it returns list value
print(filter(lambda i:False if i%2==0 else True,range(1,11))) #it returns filter object



#2) reduce
#syntax - reduce(fn,iterable)

#proper import way

from functools import reduce
print(reduce(lambda i,j :i*j,range(1,6))) # it returns factorial value of 5 bcz i*j.

