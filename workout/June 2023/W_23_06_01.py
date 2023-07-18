
#Date: 23-06-2023
#Day : Friday


print("-----------------------------",end="\n")
print("\n")
print("This is capitalize() function","\n")

#1 capitalize() --
#syntax:
#string.capitalize()

place="sathyamangalam"
print(place)
print(place.capitalize())

print("-----------------------------",end="\n")
print("\n")
print("This is endswith() function","\n")

#2 endswith() --
# #syntax:
#string.endswith(value, start, end) 

#Method 1:
string = "Hello, welcome to my world."

t = string.endswith("my world.")

print(t)

#Method 2:
string = "Hello, welcome to my world."

x = string.endswith("my world.", 5, 11)

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is casefold() function","\n")

#3 casefold() --
# #syntax:
#string.casefold() 

place="sathyamangalam"
print(place)
print(place.casefold())


print("-----------------------------",end="\n")
print("\n")
print("This is center() function","\n")

#4 center() --
# #syntax:
#string.center(length, character) 

string = "banana"

x = string.center(20, "O")

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is count() function","\n")

#5 count() -- 
#syntax:
#string.count(value, start, end)

#Maethod 1:
place="sathyamangalam"       # Output is  sathyamangalam
print(place)
print(place.count(place))

#Method 2:
place="sathyamangalam"       # Output is 5 
print(place)
print(place.count("a"))      # How many time "a" accures in the sentence


#Method 3:
place="sathyamangalam"       # Output is 3 
print(place)
print(place.count("a",3,11)) # Here "3" is starting position and "11" is ending position


print("-----------------------------",end="\n")
print("\n")
print("This is encode() function","\n")

# 6 encode() -- 
#syntax:
#string.encode(encoding=encoding, errors=errors)


place="sathyamangalam"       
print(place)
print(place.encode(encoding="ascii",errors="ignore"))


# Method 2:
place="sathyamangalam"       
print(place)
print(place.encode())

print("-----------------------------",end="\n")
print("\n")
print("This is expandtabs() function","\n")

# 7 expandtabs() -- 
#syntax:
#string.expandtabs(tabsize) default size is 8 

string = "H\te\tl\tl\to"

print(string)
print(string.expandtabs())
print(string.expandtabs(2))
print(string.expandtabs(4))
print(string.expandtabs(10))

print("-----------------------------",end="\n")
print("\n")
print("This is find() function","\n")

# 8 find() -- 
#syntax:
#string.find(value, start, end)

place="sathyamangalam"       
print(place)
print(place.find("a",8,10))

#method 2
place="sathyamangalam"       
print(place)
print(place.find("m"))

print("-----------------------------",end="\n")
print("\n")
print("This is index() function","\n")

# 9 index() -- 
#syntax:
#string.index(value, start, end)

place="sathyamangalam"       
print(place)
print(place.index("g"))

#Method 2:
place="sathyamangalam"       
print(place)
print(place.index("g",5,18))

print("-----------------------------",end="\n")
print("\n")
print("This is isalnum() function","\n")

# 10 isalnum() -- 
#syntax:
#string.isalnum()

place="sathyamangalam"       
print(place)
print(place.isalnum())

print("-----------------------------",end="\n")
print("\n")
print("This is isalpha() function","\n")

# 11 isalpha() -- 
#syntax:
#string.isalpha()

place="sathyamangalam"       
print(place)
print(place.isalpha())

print("-----------------------------",end="\n")
print("\n")
print("This is isdecimal() function","\n")

# 12 isdecimal() -- 
#syntax:
#string.isdecimal()

place="sathyamangalam"       
print(place)
print(place.isdecimal())

print("-----------------------------",end="\n")
print("\n")
print("This is isdigit() function","\n")

# 13 isdigit() -- 
#syntax:
#string.isdigit()

place="654431"       
print(place)
print(place.isdigit())

print("-----------------------------",end="\n")
print("\n")
print("This is isidentifier() function","\n")

# 14 isidentifier() -- 
#syntax:
#string.isidentifier()


a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

print("-----------------------------",end="\n")
print("\n")
print("This is islower() function","\n")

# 15 islower() -- 
#syntax:
#string.islower()



place="sathyamangalam"       
print(place)
print(place.islower())

print("-----------------------------",end="\n")
print("\n")
print("This is numeric() function","\n")

# 16 Numeric() -- 
#syntax:
#string.isnumeric()

place="sathyamangalam"       
print(place)
print(place.isnumeric())

print("-----------------------------",end="\n")
print("\n")
print("This is isprintable() function","\n")

# 17 isprintable() -- 
#syntax:
#string.isprintable()


place="sathyamangalam"       
print(place)
print(place.isprintable())


print("-----------------------------",end="\n")
print("\n")
print("This is isspace() function","\n")

# 18 isspace() -- 
#syntax:
#string.isspace()


string = "   s   "

x = string.isspace()

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is istitle() function","\n")

# 19 istitle()-- 
#syntax:
#string.istitle()


place="Sathyamangalam is My Town City. "       
print(place)
print(place.istitle())

print("-----------------------------",end="\n")
print("\n")
print("This is isupper() function","\n")

# 20 isupper() -- 
#syntax:
#string.isupper()


place="sathyamangalam"       
print(place)
print(place.isupper())

print("-----------------------------",end="\n")
print("\n")
print("This is join() function","\n")

# 21 join()-- 
#syntax:
#string.join(iterable)


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is ljust() function","\n")

# 22 ljust()-- 
#syntax:
#string.ljust(length, character)


string = "banana"

x = string.ljust(20, "O")

print(x)


print("-----------------------------",end="\n")
print("\n")
print("This is lower() function","\n")

# 23 lower() -- 
#syntax:
#string.islower()



place="sathyamangalam"       
print(place)
print(place.lower())


print("-----------------------------",end="\n")
print("\n")
print("This is lstrip() function","\n")

# 24 lstrip() -- 
#syntax:
#string.lstrip(characters)

#Method 1:

string = "     banana     "

x = string.lstrip()

print("of all fruits", x, "is my favorite")

#Method 2:

string = ",,,,,ssaaww.....banana"

x = string.lstrip(",.asw")

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is maketrans() function","\n")

# 25 maketrans() -- 
#syntax:
#str.maketrans(x, y, z)

#Method 1:

string = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(string.translate(mytable))


#Method 2:

string = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(string.translate(mytable))


#Method 3:

string = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(string.translate(mytable))

#Method 4:

string = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))


print("-----------------------------",end="\n")
print("\n")
print("This is partition() function","\n")

# 26 partition() -- 
#syntax:
#string.partition(value)


string = "I could eat bananas all day"

x = string.partition("apples")

print(x)


print("-----------------------------",end="\n")
print("\n")
print("This is replace() function","\n")

# 27 replace() -- 
#syntax:
#string.replace(oldvalue, newvalue, count)

#Method 1:

string = "one one was a race horse, two two was one too."

x = string.replace("one", "three")

print(x)


#Method 2:

string = "one one was a race horse, two two was one too."

x = string.replace("one", "three", 2)

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is rfind() function","\n")

# 28 rfind() -- 
#syntax:
#string.rfind(value, start, end)

#Method 1:

string = "Hello, welcome to my world."

x = string.rfind("e", 5, 10)

print(x)

#Method 2:

string = "Hello, welcome to my world."

print(string.rfind("q"))

print("-----------------------------",end="\n")
print("\n")
print("This is rindex() function","\n")

# 29 rindex() -- 
#syntax:
#string.rindex(value, start, end)

#Method 1:

string = "Hello, welcome to my world."

x = string.rindex("e", 5, 10)

print(x)

#Method 2:

string = "Hello, welcome to my world."

x = string.rindex("e")

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is rjust() function","\n")

# 30 rjust() -- 
#syntax:
#string.rjust(length, character)


string = "banana"

x = string.rjust(20, "O")

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is rpartition() function","\n")

# 31 rpartition() -- 
#syntax:
#string.rpartition(value)

string = "I could eat bananas all day, bananas are my favorite fruit"

x = string.rpartition("apples")

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is rstrip() function","\n")

# 32 rsplit()-- 
#syntax:
#string.rsplit(separator, maxsplit)


string = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = string.rsplit(", ", 1)

print(x)


print("-----------------------------",end="\n")
print("\n")
print("This is rstrip() function","\n")

# 33 rstrip() -- 
#syntax:
#string.rstrip(characters)

string = "banana,,,,,ssqqqww....."

x = string.rstrip(",.qsw")

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is split() function","\n")

# 34 split() -- 
#syntax:
#string.split(separator, maxsplit)

#Method 1:

string = "hello, my name is Peter, I am 26 years old"

x = string.split(", ")

print(x)

#Method 2:

string = "apple#banana#cherry#orange"

x = string.split("#")

print(x)

#Method 3:

string = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = string.split("#", 1)

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is splitlines() function","\n")

# 35 splitlines() -- 
#syntax:
#string.splitlines(keeplinebreaks)

string = "Thank you for the music\nWelcome to the jungle"

x = string.splitlines(True)

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is startswith() function","\n")

# 36 startswith() -- 
#syntax:
#string.startswith(value, start, end)


string = "Hello, welcome to my world."

x = string.startswith("wel", 7, 20)

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is strip() function","\n")

# 37 strip()-- 
#syntax:
#string.strip(characters)


string = ",,,,,rrttgg.....banana....rrr"

x = string.strip(",.grt")

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is swapcase() function","\n")

# 38 swapcase() -- 
#syntax:
#string.swapcase()

string = "Hello My Name Is PETER"

x = string.swapcase()

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is title() function","\n")

# 39 title() -- 
#syntax:
#string.title()

#Method 1:

string = "Welcome to my 2nd world"

x = string.title()

print(x)


#Method 2:

string = "hello b2b2b2 and 3g3g3g"

x = string.title()

print(x)

print("-----------------------------",end="\n")
print("\n")
print("This is translate() function","\n")

# 40 translate()-- 
#syntax:
#string.translate(table)


string = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(string.translate(mytable))


print("-----------------------------",end="\n")
print("\n")
print("This is upper() function","\n")

# 41 upper() -- 
#syntax:
#string.upper()

string = "Hello my friends"

x = string.upper()

print(x)


print("-----------------------------",end="\n")
print("\n")
print("This is zfill() function","\n")

# 42 zfill() -- 
#syntax:
#string.zfill(len)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
print("\n")

