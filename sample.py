'''
output=2
'''

def most_repeat_num(l1):
    d={}
    for num in l1:
       d[num]=d.get(num,0)+1
    for k,v in d.items():
        count=0
        if v>count:
            count=v

    return count


l1=[1,2,2,3,4,5,6,2,1,3,5,6,7,9]

print(most_repeat_num(l1))

















import sys
sys.exit(0)
'''
WAP to reverse internal content of every second world present in the given string

s="one two three four five six seven"
l=s.split()
# print(l)
i=0
l1=[]
while i < len(l):
    if i % 2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
output=" ".join(l1)
print(output)

'''



