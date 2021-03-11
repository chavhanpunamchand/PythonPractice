def decor(func):
    def inner(x, y):
        print("Before function execution")
        func(x, y)
        print("After function execution")

    return inner

@decor
def sum(x, y):
    result = x + y
    print(result)

sum(10,20)
