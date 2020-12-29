'''
Regular expression is used to search from the string
re module available
'''



import re
pattern="Punamchand"
string1="Punam"

# result=re.match(string1,pattern) #to match the string at begining of target string
result=re.fullmatch(string1,pattern)# to match the complete string, if matched return true

if result:
    print("Match successful")
else:
    print("Not matched")



import sys
sys.exit(0)
import re
count=0

pattern=re.compile("ab") #example from durga sir notes

matcher=pattern.finditer("abaababa")

for match in matcher:
    count+=1
    print(match.start(),"...",match.end(),"...",match.group())

print("The number occerance is :",count)
