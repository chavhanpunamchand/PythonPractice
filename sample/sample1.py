
# 0,1,1,2,3,5,8,13,21....

nth_term=int(input("How any term ?: "))

fnum=0
snum=1
result=0
if nth_term <=0:
    print("enter positive num ")
elif nth_term ==1:
    print("The fabonaci series of 1 is",fnum)
else:
    while nth_term>0:
        print(fnum,end=" ") # 0,
        result=fnum + snum # 1, 0, 1
        fnum=snum  #1
        snum=result #1
        nth_term =nth_term -1


import sys
sys.exit(0)

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1










num=int(input("Enter the multi- table num: "))

print("Table of ",num)
for i in range(1,11):
    print(i*num)




# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
# print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
print(f'{kilometers} kilometers is equal to {miles} miles')