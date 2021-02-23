
def addelemfinder(l1):
    nlist=[]
    for i in range(len(l1)):
        for j in range(i):
            ans=l1[i]+l1[j]
            if ans==15:
                nlist.append(l1[i])
                nlist.append(l1[j])
    return nlist

l1=[2,8,10,3,12,10,2,13]
# l4=set(l1)

nl1=addelemfinder(l1)
s1=set(nl1)
fans=list(s1)
print(fans)





# import random
#
# l1=[ item for item in range(1000)]
#
# print(l1[999:990:-1])


# l1=[1,2,3,4,5,6,7,8,9,10]
#
# l2=[5,6,10,12,13,14]
#
# l3=[102,103,104,105,5,6]

# ans=set(l1) & set(l2) & set(l3)
#
# print(list(ans))

# print(l[0:len(l):2])
# i=0
# while i <=(len(l)-1):
#     print(l[i],end=" ")
#     i=i+2

# for i in range(len(l)-1):
#     if i %2==0:
#         print(l[i],end=" ")
#

