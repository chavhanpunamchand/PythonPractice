'''

hash table --

key-value pair

{'key':'value','key2':'val2'}

key duplicate allowed
hetro
insertion
mutable
dynamic
intexing and slicing

'''
list1=[(10,"R"),(20,"30"),(40,50)]
d=dict(list1)
print(d)
# print(len(d))
# d.clear()
# print(d)
# print(d.get(10))

# print(d.pop(30))
# print(d)
# print(d.popitem())
# print(d.keys())
# print(d.values())
# print(d.items())
d.setdefault(30,"49")
print(d)
print(d.setdefault(10,"P"))














import sys
sys.exit(0)

rec={'Rahul': '90', 'Pawan': '98', 'Punamchand': '40'}
rec['Rahul']=80
print(rec)

del rec['Rahul']

print(rec)









rec={}
n=int(input("Enter num of student: "))
i=1
while i<=n:
    name=input("Enter the name: ")
    marks=input("Enter % marks of stud: ")
    rec[name]=marks
    i=i+1
print(rec)

# print(rec["punamchand"])






dict1={}

dict1[100]="Ravi"
dict1[200]='Rahul'
dict1[300]='Pawan'

print(dict1)

print(dict1[100])






