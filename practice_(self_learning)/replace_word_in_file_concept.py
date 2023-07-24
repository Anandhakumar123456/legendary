import while_01 as wh


"""
#Writing lines in a file:

f=open("sample.txt","w")
f.write("line1\nline2\nline3\nline4\n")
f.close()


#Reading and replacing string in a same file.

f=open("sample.txt","r")
d=f.read()
d=d.replace("line3","this line is replaced for line 3.")
f.close()

f=open("sample.txt","w")
f.write(d)
f.close()

"""

"""
def make_sum(i):
    return i+1

ot=map(make_sum,range(20))
for i in ot:
    print(i)"""


def type9():
    try:
        wh.all_function()
    except Exception as er:
        print(er)
    finally:
        print("Completed....")    


type9()