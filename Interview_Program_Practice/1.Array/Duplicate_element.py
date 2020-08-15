'''
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list.
One of the integers is missing in the list. Write an efficient code to find the missing integer.

'''
def printgetDuplicate(A):
    n=len(A)
    print("The repeating element are:",end="")
    for i in range(n):
        for j in range(i+1,n):
            if A[i]==A[j]:
                print(A[i],end=",")




#Here main program
A=[1,5,6,7,9,1,8,5]
printgetDuplicate(A)
#print("The duplicate element is :",dInt)