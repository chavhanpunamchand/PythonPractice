'''
List Overlap
Exercise 5 (and Solution)
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Extras:
1.	Randomly generate two lists to test this
2.	Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

'''
def listOverlap(ls1,ls2):
    fls=[]
    for elmt1 in ls1:
        for elmt2 in ls2:
            if elmt1==elmt2:
               fls.append(elmt1)
    return fls
# input two difference list
ls1=[]
ls2=[]
addNum=int(input('Enter the num of element you want to add in list: '))
for i in range(1,addNum+1):
       e1=input("Enter the list element : ")
       ls1.append(e1)
print(ls1)
for j in range(1, addNum + 1):
      e2=input("Enter the element add in ls2: ")
      ls2.append(e2)
print(ls2)
print("List overlap element is: ",listOverlap(ls1,ls2))

