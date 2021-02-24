
def two_num_division(x,y):
    try:
        result=x/y

    except ZeroDivisionError as msg:
        return msg
    else:
        return result



x=int(input("Enter first number: "))
y=int(input("Enter second number:  "))

result=two_num_division(x,y)
print(result)
