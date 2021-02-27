"""

WAP to find the second largest number in list without sorted, max and min function

"""

l1=[20,67,3,2,6,7,74,90,109,100,6,5,9,2,3,67,10,45]
new_num=set(l1)
new_list_num=list(new_num)
print(new_list_num)

if new_list_num[0]>new_list_num[1]:
    m,m2=new_list_num[0],new_list_num[1]
else:
    m,m2=new_list_num[1],new_list_num[0]

for x in new_list_num[2:]:
    if x >m2:
        if x>m:
            m2,m=m,x
        else:
            m2=x

print(m2)