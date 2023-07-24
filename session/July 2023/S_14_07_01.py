#Date: 14-07-2023
#Day : Friday

#file operations 
#WRA -write,read,append


#writing in a file:
f=open("sample.txt","w")
f.write("line1\nline2\n")
f.close()

#reading in a file:

f=open("sample.txt","r")
print(f.readlines())
f.close()


#appending in a file:  - adding lines :

f=open("sample.txt","a")
f.write("line3\nline4\nline5\nline6\n")
f.close()


#creating a python file and writing the codes in a file:
p=open("main.py","w")
p.write("txt=hello world")
p.close()

print(p.readlines)