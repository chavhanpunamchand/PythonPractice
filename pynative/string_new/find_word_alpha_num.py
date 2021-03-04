""" find word with both alphabet and numbers """
str1="Emma25 is data scientiest50 and AI Expert"

print("The original string is :",str1)

res=[]
temp=str1.split()
for item in temp:
    if any( char.isalpha() for char in item) and any( char.isdigit()  for char in item):
        res.append(item)

print("Diplay the word with alphabet and number ")

for i in res:
    print(i)