mydict={}

for i in range(1,3):
    username=input(f"Enter the Username for user {i}: ")
    password=input(f"Enter the Password for user {i}: ")
    mydict[username.title()] = password


#    mydict={username.title():password}      
#    This case is represent to store the values in the dictionary. //   and .title() represent the username convert the capital letter of the first letter. 

# !!!! Note : This method is only stores the last entered the values. 

print(mydict)



"""
To check if a key-value pair exists in a dictionary, i.e., if a dictionary has a pair, use the in operator and the items() method. Specify a tuple (key, value). Use not in to check if a pair does not exist in a dictionary.



To check if a value exists in a dictionary, i.e., if a dictionary has a value, use the in operator and the values() method. Use not in to check if a value does not exist in a dictionary.


d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

print(('key1', 'val1') in d.items())
# True

print(('key1', 'val2') in d.items())
# False

print(('key1', 'val2') not in d.items())
# True

"""