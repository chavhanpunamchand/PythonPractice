#function of nth fibonacci number

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    #first fibonacci number is 0
    elif n==0:
        return 0
    #second fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)  

#driver program
print(Fibonacci(9))               

        