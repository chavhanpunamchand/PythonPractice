"""

"""
import re
s='''Punamchand is a good boys and age is 27 and he is software developer chavhapunamchand@gmail.com Vivek pramdas Rathod age is 28 viky123@yahoo.com '''

s1="ABCDEFG"

# m=re.match('^[A-Z][a-z]+', s)

# m=re.fullmatch('[ABCDEFG]', s1)

# m=re.findall('[A-Z][a-z]+', s)

# m=re.fullmatch('[A-Z][a-z]+', s)

# m=re.finditer('[A-Z][a-z]+', s)
# for item in m:
#     print("Search",item)

# m=re.subn("[A-Z][a-z]+","*****",s)
# print(m)

m=re.split('\s',s)

for i in m:
    print(i)


