print("Statement-1")
try:
    print(10/0)
except ZeroDivisionError as msg:
    print(msg)
    print(10/2)
finally:
    print("This is simple flow of exception")




