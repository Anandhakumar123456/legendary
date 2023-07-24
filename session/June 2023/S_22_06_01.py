
#Date: 22-06-2023
#Day : Thursday

#----------------------Topic-------------------

#5) skip/step
#syntax - idfname[strting_index : stop_index +1 :skip value ]
# This is skip the index and it's value

program="python program"


print(" p y t h o n       p  r  o  g   r  a   m")
print(" 0 1 0 1 0 1   0   1  0  1  0   1  0   1 \n")
print(program[0::2],"\n")  # it prints value 0 of the index 
# Output is : pto rga 


print(" p y t h o n       p  r  o  g   r  a   m")
print(" 0 1 0 1 0 1   0   1  0  1  0   1  0   1 \n")
print(program[1::2],"\n")  # it prints value 1 of the index 
# Output is : yhnporm  



print(" p y t h o n       p  r  o  g   r  a   m")
print(" 0 1 2 0 1 2   0   1  2  0  1   2  0   1 \n")
print(program[1::3],"\n")  # it prints value 1 of the index 
# Output is : yopgm



# 6 string is immutable (can not change its value)

# 7 Format strings

#f-string , format() , % 

# 1) f-string   

name="anand"
place="sathy"

message=f"Iam {name}. and iam from {place}."
print(message)

# b) format()
# b) format() --Method 1

print("**********************************")
message="Iam {}. and iam from {}.".format(name,place)
print(message,end="\n\n")



# b) format() --Method 2 -- using = sign
message="Iam {user}. and iam from {city}.".format(user=name,city=place)
print(message,end="\n\n")




# b) format() --Method 3 -- using Index value
message="Iam {0}. and iam from {1}.".format(name,place)
print(message,end="\n\n")



# % operator

message="Iam %s. and iam from %s."%(name,place)
print(message,end="\n\n")


# 8) check built-in function for place variable :

#print(dir(place))