"""
fabonancci series


"""

nterm = int(input("Enter the nth term series : "))
num1=0
num2=1
result=0
if nterm<=0:
    print("Enter positive number ")
elif nterm==1:
    print("Fabonancci series is :",num1,num2)

else:
    while nterm >=1:
        print(num1 ,end=" ")
        result=num1+num2
        num1=num2
        num2=result
        nterm=nterm-1

