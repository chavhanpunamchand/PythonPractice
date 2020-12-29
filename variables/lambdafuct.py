'''
squreit

'''


g=lambda a,b: a if a>b else b
v=g(10,20)
print("graetest num",v)




import sys
sys.exit(0)

s=lambda x:x%2==0
v=s(10)
if v:
    print("given num is even",v)




list1=[10,20,30,65,54,89,76,51]
list2=list(filter(lambda x:x%2==1,list1 ))
print(list2)
# for i in list2:
#     print(i)


g=lambda a,b: a if a>b else b
print('Biggest number from the given num :',g(10,20))

s=lambda a,b:a+b
print("The sum of two num is: ",s(10,20))






def squreit(n):
    a=10
    print(a)
    return n*n

s=lambda n:n*n

print(s(4))
a=squreit(4)
print(a)