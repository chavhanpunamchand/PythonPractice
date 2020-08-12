n=int(input("Enter the number of row: "))
for i in range (1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-j),end=" ")
    print()    