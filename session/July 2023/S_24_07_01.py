#Date: 24-07-2023
#Day : Monday


"""
closure decorators

1) fn enclosed function.
2) enclosed should return nested fn
3) Nested fn should use enclosed fn parameter.

"""



def sample(value):
    def innerfn(value2):
        return value+value2
    return innerfn

obj=sample(6)
del sample  #delete the sample function
print(obj(5))


#decorator function without changing original function and its coding.That is called Decorators.

def deco(fn):
    def innerfn(value):
        print("Good Morning!")
        print(fn(value))
    return innerfn


@deco #This method is calls the inner fn
def greeting(user):
    return f"Hello!! {user}"

greeting("anand")
#obj = deco(greeting)
#obj()