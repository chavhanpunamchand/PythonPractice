import time

def decor(func):
    def inner(x,y):
        print("Before function execution time is :",round(time.time(),2))
        func(x,y)
        print("After function execution time is :",round(time.time(),2))
    return inner

@decor
def sum(x,y):
    print(f"Sum of {x} and {y} is :",x+y)

sum(10,20)