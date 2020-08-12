# Linearly searching  x in arr[]
# If x is present then return its loacation
# otherwisw return -1

def search(arr,n,x):
    for i in range(0,n):
        if(arr[i]==x):
            return i

    return -1

# Driver code
arr=[2,6,9,46,10,7,64,46,12,85,20,30,40] 
x=30
n=len(arr)  
result=search(arr,n,x)
if result== -1:
    print("The element not presrnt in array ")
else:
    print("The element present at index :",result)             