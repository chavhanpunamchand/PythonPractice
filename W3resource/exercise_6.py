"""
Write a Python program which accepts a sequence of comma-separated numbers
from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
data = "3,5,7,23"
output=data.split(",")
print(output)
print(type(output))

t1=tuple(output)
print(t1)
print(type(t1))



