def decor(func):
    def inner():
        a = func()
        add = a + 5
        return add

    return inner


@decor
def num():
    return 10


result = num()
print(result)
# result_func=decor(num)
# print(result_func())
