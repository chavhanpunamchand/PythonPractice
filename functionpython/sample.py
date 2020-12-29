
'''
1. position as arg
2.keyword as arg
3.default as arg
4.variable leght as arg
'''



def oddeven(num):
    if num%2==0:
        print("given num is even",num)
    else :
        print("given num is odd",num)

oddeven(4)
























import sys
sys.exit(0)

def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("Sum =",total)


sum()
sum(10)
sum(10,20)

list




1
def add(**n):
    print("a :",a)
    print("b :",b)
    print("c :",c)
    sum=a+b
    return sum

add(a=-10,b=39)


def fact(num):
    b=num
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result,b

factor1,n=fact(5)
print(factor1)
print(n)



def squareval(num):
    num*num
    return


ans=squareval(4)
print(ans)
ans1=squareval(5)
print(ans1)

ans2=squareval(6)
print(ans2)









def wish(name):
    print("Hello",name,"Good Morning")

wish("Pawan")
wish("Punam")




def data_rep():
    a=3
    for i in range(a):
        print(556)

def data_rep1():
    a=4
    for i in range(a):
        print(666)


data_rep()
data_rep1()

#
#
# print(556)
# print(556)
# print(666)
# print(666)
# print(666)
# print(666)
# print(556)
