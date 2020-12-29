
def AvgNum(N):
    sum=0
    for i in range(1,N+1):
        sum=sum + i
    return sum/N

N=int(input("Enter the average num value: "))
print("Average of "+str(N)+" is",AvgNum(N))












