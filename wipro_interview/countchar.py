
def count_item(l):
    l1=[]
    d={}
    for char in l:
        if char not in l1:
            l1.append(char)
    for item in l1:
        t=l.count(item)
        d[item]=t
    return d

l=[1,1,1,5,5,4,6,7,7,9]
print(count_item(l))