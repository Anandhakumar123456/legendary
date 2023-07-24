#Date: 28-06-2023
#Day : Wednesday

#---------------------Data types--------------------------
# Dictionary:

#1) Empty dictionary
d={}
d=dict()


#2) ex--

d={
    "colors":"red",
    "number":1
    }


#3) key--
# immutable - tuple,string,integer
#no duplicate,accept last value it duplicate

#Ex

d={
    "a":1,
    "b":1,
    "a":3
    }

print(d)

#value
#any data type can be value
#duplicate are also last

d={"color":"red",
    "number":1}
print(type(d))


d={"a":1,"b":2,"c":2,"a":4}
print(d)



d={"blue":1,"red":2,"orange":5}
print(d)
#syntax: idfname[key]

print(d["blue"])

#update
#syntax: idfname[key] = value

d["orange"] =3
print(d)



#Delete the value

del d["red"]



#------------------------set data type---------------------#

a=set()
a.update("apple","apple","orange","banana")
print(a)

print(dir(a))

#Boolean

a=True
b=False

print(True == 1)  #True  
print(False == 0) #True
print(False == 1) #False
print(type(a))

#None data type
a=None
print(type(a))
a=""
print(type(a))