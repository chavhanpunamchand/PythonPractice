'''
Factorial of non-negative integer n,denoted by n! is the
product of all positive integer less than or equal to n...

one way:----
import math
n=int(input("Enter the factorial number:"))

fact=math.factorial(n)
print(fact)

Second way by recursive method:-
def factor(n):
    if n==0:
        return 1
    else:
        return n*factor(n-1)


n=int(input("Enter factorial number: "))
fact=factor(n)
print("Factorial of ",n,"is",fact)

Third way loop
'''
n=int(input("Enter the factorial num:"))
result=1
for i in range(n,0,-1):
    result=result*i

print("The factorial of ",n,"is ",result)







