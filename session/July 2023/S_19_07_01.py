#Date: 19-07-2023
#Day : Wednesday

#Test Total marks 20:


print(type(""))
print(type("[]"))
print(type(5+5.0))

print(max(1,1.0))
a=[1,2,3]
b=(1,2,3)

a.remove(2)
print(a)


print("Father of python is Guido Van Rossum.")
print("Reverse a string or number.")
txt="Anandhakumar"[::-1]   #This means reverse a string or number in simple way.
print(txt)


a="7"
b=a+"0"
c=int(b)
d=float(c)
print(d)




a="2"
b='2'
c=a+b
print(c)



#a=10,b=12,c=5     #is is not valid.

a,b,c=10,12,5     #it is a valid variable declaration.
if (a>b) and (a>c):
    print("A is bigger.")
elif (b>c) and (b>a):
    print("B is bigger.")    
else:
    print("C is bigger.")


x=1#2#3

print(x)

sample_list=[1,2,3,4,5,6]

print(sample_list.index(4))

