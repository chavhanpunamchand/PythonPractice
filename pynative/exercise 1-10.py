"""
Question 10: Given a two list of numbers create
a new list such that new list should contain only odd numbers from the first list
and even numbers from the second list

First List  [10, 20, 23, 11, 17]
Second List  [13, 43, 24, 36, 12]

result List is [23, 11, 17, 24, 36, 12]
"""
first_list = [10, 20, 23, 11, 17]

second_list = [13, 43, 24, 36, 12]

result_list=[]

for item in first_list:
    if item%2==1:
        result_list.append(item)

for num in second_list:
    if num%2==0:
        result_list.append(num)

print("result list is",result_list)






import sys
sys.exit(0)

"""
Question 9: Reverse a given number and return true
if it is the same as the original number

original number 121
The original and reverse number is the same

original number 125
The original and reverse number is not same

"""
o_num=int(input("Enter original number : "))
print("original number ",o_num)

num1=str(o_num)
num2=num1[::-1]
if num1==num2:
    print("The original and reverse num is the same")
else:
    print("The original and reverse num is not same")

# print(num2)

# list1=list(o_num)
# print(list1)

# list2=list1.reverse()
# print(list2)

# r_num=reversed(o_num)
# print(r_num)






"""
Question 8: Print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

for j in range(1, 6):
    for i in range(j):
        print(j, end=" ")
    print()



"""
    Question 7: Return the total count
    of sub-string “Emma” appears in the given string
    Given string is “Emma is good developer. Emma is a writer”

    Emma appeared 2 times

 """
str1 = "Emma is good developer.Emma is a writer"
print("Emma appeared",str1.count("Emma"),"times")



"""
Question 6: Given a list of numbers,
Iterate it and print only those numbers which are divisible of 5

Given list is  [10, 20, 33, 46, 55]
Divisible of 5 in a list
10
20
55

"""

list1 = [10, 20, 33, 46, 55]
print("Divisible of 5 in a list ")
for num in list1:
    if num % 5 == 0:
        print(num)

    else:
        pass




"""
Question 5: Given a list of numbers,
return True if first and last number of a list is same

Given list is  [10, 20, 30, 40, 10]
result is True

"""

def check_list(list2):
    if list2[0]==list2[-1]:
        return True

list1=[10,20,30,40,10]
print("Given list is :",list1)
print("result is ",check_list(list1))



"""
Question 4: Given a string and an integer number n,
remove characters from a string starting from zero up to n and return a new string
For example, removeChars("pynative", 4) so output must be tive.
 Note: n must be less than the length of the string.

"""
def removeChar(str1,n):
    return str1[n::]


print("Removing n number of chars")
str2=removeChar("pynative",4)
print(str2)



"""
Question 3: Given a string, display only those
characters which are present at an even index number.
"""
str = "pynative"
print("Orginal String is ",str)
print("Printing only even index chars")
# char=str[0::2]
# print(char)

for i in range(0,len(str),2):
    print(str[i])


"""
Question 2: Given a range of first 10 numbers,
Iterate from start number to the end number and
print the sum of the current number and previous number
"""
print("Printing current and previous number sum in a given range(10)")

p_num=0
c_num=0
for i in range(0,10):
    c_num=i
    print(f"Current Number {c_num} Previous Number {p_num} Sum: {c_num + p_num}")
    p_num=i

"""
Question 1: Given a two integer numbers return their product
and  if the product is greater than 1000, then return their sum
"""


def add_product(x1, y1):
    z = x1 * y1
    if z > 1000:
        return x1 + y1
    else:
        return z


x, y = input("Enter the two num: ").split()
a = int(x)
b = int(y)

output = add_product(a, b)
print(output)
