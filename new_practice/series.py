""" fabonancci Series """

n=int(input("Enter the number of sequence you want: "))

n1=0
n2=1
ntemp=0
if n<=0:
    print("enter positive number ")
elif n==1:
    print("fabonanci series is :",n2)
else:
    while n>=1:
      print(n1,end=" ")
      ntemp=n1+n2
      n1=n2
      n2=ntemp
      n=n-1






