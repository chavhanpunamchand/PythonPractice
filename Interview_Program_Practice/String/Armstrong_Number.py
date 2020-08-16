'''
number of n digit which are equal to sum of nth power of its digit
5----nth power is 1 then 5nth 1 nth power is 5 ,therefore number is armstrong

153 --
'''
for i in range(1001):
    num=i
    n=len(str(i))
    result=0
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if result==num:
        print(num)

