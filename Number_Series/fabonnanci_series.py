nterm=int(input("Enetr the nth term fabonnaci series: "))
n1=1
n2=2
count=0
nth=0
if nterm<=0:
    print("Enter the positive integer")
elif nterm==1:
    print("The fabonaci series is :",nterm)
else:
    while count<nterm:
        nth=n1+n2
        print(n1,end=" ")
        n1=n2
        n2=nth
        count+=1        
