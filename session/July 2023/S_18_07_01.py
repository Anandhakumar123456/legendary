#Date: 18-07-2023
#Day : Tuesday

#Error Handling:

def odd_even(i):
    try:
        if i %2 ==0:
            return "Even"
        else:
            return "Odd"
    except:
        return "An Error Occured."

print(odd_even(5))
#print(odd_even("apple"))


#Individual Error handling:
def odd_even(i):
    try:
        l=[]
        l[4]
        if i %2 ==0:
            return "Even"
        else:
            return "Odd"
    except IndexError:  #it returns index error only.
        return "Index Error"
    except TypeError: #it returns Type error only.
        return "Type Error Occured."
    except Exception as err_msg:  #it is all errors in this type.
        return err_msg

print(odd_even(5))



#Raising Error using raise keyword.

def odd_even(i):
    try:
        if type(i) is int:
            if i %2 ==0:
                return "Even"
            else:
                return "Odd"
        else:
            raise Exception("Value should be integer.")     #This is raising error.
    except IndexError:  
        return "Index Error"
    except TypeError: 
        return "Type Error Occured."
    except Exception as err_msg:  
        return err_msg

print(odd_even(5))

