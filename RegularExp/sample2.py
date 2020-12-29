import re
# 5.finditer():
# return the iterator yielding a match object for each match

t=re.finditer("[a-z]","aaaa7b9c5k8z")
for m in t:
    print(m.start(),"...",m.end(),"....",m.group())




import sys
sys.exit(0)
# 4.findall() to find all occurence of the match

i=re.findall("[0-9]","a7b9c5kz")
print(i)



import sys
sys.exit(0)

#3.search()

s=input("Enter input char you check:")
m=re.search(s,"abaaaba")
if m:
    print("Match is available")
    print("first occurence of match start with index ",m.start(),"end index:",m.end())
else:
    print("match not available")
