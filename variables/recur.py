'''
factorial with recursive

'''

result=0
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print("factorial of 4 is :",factorial(5))
