"""
Python facilitates us to not specify the exception with the except statement.

We can declare multiple exceptions in the except statement
 since the try block may contain the statements which throw the different type of exceptions.

We can also specify an else block along with the try-except statement,
 which will be executed if no exception is raised in the try block.
 
The statements that don't throw the exception should be placed inside the else block.
"""



import sys
sys.exit(0)


import time

time.sleep(5)
try:
    raise KeyboardInterrupt
finally:
    print('welcome, world!')





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
