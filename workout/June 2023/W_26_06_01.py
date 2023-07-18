#Date: 26-06-2023
#Day : Monday



#Number systems


#Binary Number system

"""
    Binary Number system is with the base or radix '2' is known as binary number system. It repersent the 0 and 1.

    for example:
        a= 1001 base 2
"""
b="1001"
print("Binary to decimal",b,":",int(b,2))



#Octal Number system

"""
    Octal Number System is  one in which the base value is '8'. It uses 8 digits i.e 0-7 for the creation of Octal Numbers.  It also a positional system i.e weighty is assigned to each position.

        for eg. o=0o123 base 8
"""

o=0o123
print("Octal to binary ",o,":",bin(o))

#Decimal Number system

"""
    A number system with a base value of '10' is termed a Decikal number system. and it is represented using digits between 0-9 .

    for eg:
        a=10 base 10
"""


a=10
print("Decimal to binary",a,":",bin(a))

a=1254
print("Decimal to Hexadecimal",a,":",hex(a))


#Hexa decimal Number system

"""
A number system with a base of 16 is called a hexadecimal number system.
It represented using numbers between 0-9 and the alphabets between A to F. As both numeric digits and alphabets are used in this system, it is also called an alphanumeric system.

for eg:
        a= face base 16

"""

a=0xface
print("Hexadecimal to binary ",a,":",bin(a))

