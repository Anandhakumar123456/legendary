
#Date: 03-07-2023
#Day : Monday


a=4
b=bin(a)


print(bin(a))
print(oct(a))
print(hex(a))



print(hex(int(bin(a),base=2)))   
print(int(oct(a),base=8))
print(int(bin(a),base=16))


print(4^2)
print(4&2)
print(4|2)
print(4<<2)
print(4>>2)
print(~2)    #These needs two operations //1) increment by one +1 // 2) change the sign


#PEMDAS rule  Operator precedence:

print((4+4)/4)    #first precedence is (4+4)  ! Inner brackets.
print(((((20+5)*2)-5)/2)-12)  #first precedence is (20+5).  

