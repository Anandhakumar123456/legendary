#Date: 12-07-2023
#Day : Wednesday


#LEGB rule
#local
#enclosed 
#global
#built-in
a=1
def fun1():
    b=2
    print(f"function scope a-{a}")
    print(f"function scope b-{b}")
    def fun2():
        c=3
        print(f"function scope a-{a}")
        b=4
        print(f"function scope b-{b}")
        print(f"function scope c-{b}")
    fun2()
fun1()
print(f"global scope - {a}")


