'''
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list.
 One of the integers is missing in the list. Write an efficient code to find the missing integer.

'''

def getMissingInt(A):
    n = len(A)
    totalSum = (n + 1) * (n + 2) / 2
    print(totalSum)
    #lsum= sum(A)
    lsum=0
    for i in range(n):
        lsum=lsum+A[i]
    print(lsum)

    return totalSum - lsum




# Array are given
A=[1,2,3,9,8,6,4,7]
missInt=getMissingInt(A)
print("The missing integer are :",missInt)