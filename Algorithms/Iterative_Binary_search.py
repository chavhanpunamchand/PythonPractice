#Python program for iterative binary search.
#Retrun index of x in arr if present, else -1

def binarySearch(arr,l,r,x):
    #check base case
    while l <= r:
        mid= l +(r-l)//2
        # if the element present at middle itself
        # itself

        if arr[mid]==x:
            return mid
        # If element is smaller than mid,
        # then
        # it can only present in left subarray
        elif arr[mid]<x:
            l=mid+1 

        else:
            r=mid-1     

    
        # Element not present in array
    return -1

# Driver code
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13]    
x= 15
#function call
result=binarySearch(arr,0,len(arr)-1,x)
if result != -1:
    print("Element is present at index :",result)   
else:
    print("The element not present in array")    
               
