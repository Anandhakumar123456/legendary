#Date: 07-07-2023
#Day : Friday


for i in range(1,11):
    if i==3:
        continue
    elif i==6:
        break
    else:
        pass
    print(i)

print("-----------------User defined function------------------")
# user defined function
# syntax:
def sample(a,b):
    return a+b

print(sample(20,10))
print(sample(30,50))
print(sample(100,200))
print(type(sample))
