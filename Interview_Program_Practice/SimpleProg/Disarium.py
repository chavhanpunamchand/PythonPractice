'''
Gnum=1759
Num=0
l= length(Number)=4
#last digit of num  ---- This is in loop
L=4
zeros=l-2
divisor=int(“1+zeros”)
1759/Divisor= remainder
Num=Num+remainder **l
If Gnum==Num:
Print(“Given num disiarium”)
Else:
Print(“Given num is not disiarium”)
Program to determine whether a given number is a Disarium number

'''
def disarium(num):
    #calculate the lenght
    sum=rem=0
    n=num
    l=len(str(num))

    # Calculates the sum of digits powered with their respective position
    while (num > 0):
        rem = num % 10
        sum = sum + int(rem ** l)
        num = num // 10
        l = l - 1

    if n==sum:
        print(n,"is Disarium")
    else:
        print(n,"is not disarium ")

num=int(input("Enter the num check for disarium: "))
disarium(num)
