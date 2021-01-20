'''
5. Write a Python program which accepts
the user's first and last name and print them in reverse order with a space between them.


6. Write a Python program which accepts a sequence of comma-separated
numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

# fname=input("Enter first name :")
# lname=input("Enter last name :")
#
# print("Hello "+lname+" "+fname)

numbers=input("Enter the sequence of number :")

list1=numbers.split(",")
tuple1=tuple(list1)
print("List convertion :",list1)
print("tuple convertion :",tuple1)



