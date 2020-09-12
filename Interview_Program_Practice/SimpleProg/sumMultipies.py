'''
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
'''

def sumMulti(limit):
    ls=[]
    for num in range(1,limit+1):
        if num%3==0 and num%5==0:
            ls.append(num)
        elif num%3==0:
            ls.append(num)
        elif num%5==0:
            ls.append(num)

    return ls
a=int(input("Enter the limit: "))
print("Sum of Multiplies is",sumMulti(a))