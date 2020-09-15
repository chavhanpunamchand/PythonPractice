'''
Program to find GCD or HCF of two numbers
GCD (Greatest Common Divisor) or
HCF (Highest Common Factor) of two numbers is the largest number that divides both of them.

'''
def GCD(a,b):
    #Every thing divisor of zero
    if a==0:
        return b
    if b==0:
        return a
    #take the empty list
    fs1NumDivisor=[]
    fs2NumDivisor=[]
    for i in range(1,a+1): # calculate a num divisor
        if a%i==0:
            fs1NumDivisor.append(i)
    for j in range(1,b+1): # calulate b num divisor
        if b%j==0:
            fs2NumDivisor.append(j)
    # comman element in between both
    fs3CommanNum=[]
    for item1 in fs1NumDivisor:
        for item2 in fs2NumDivisor:
            if item1==item2:
                fs3CommanNum.append(item1)
    #multiply common number
    GDC=max(fs3CommanNum)
    return GDC
try:
    a=int(input("Enter the fs1 Num: "))
    b=int(input("Enetr the fs2 num: "))
except:
    print("Please enter proper value formate")
else:
    print("Gretestb common divisor or (HCF) of two number is: ",GCD(a,b))




