"""
Question 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.

Expected Output:

Case 1:

base = 2
exponent = 5

2 raises to the power of 5 is: 32 i.e. (2 *2 * 2 *2 *2 = 32)

Case 2:

base = 5
exponent = 4

5 raises to the power of 4 is: 625 i.e. (5 *5 * 5 *5 = 625)
"""

def exponent(base,exp):
    power=1
    for i in range(1,exp+1):
        # base=base*exp
        power=base*power

    print(f"{base} raises to power of {exp} is :",power)


exponent(5,4)





import sys
sys.exit(0)
"""
Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)
* * * * *
* * * *
* * *
* *
*

"C:\My Data\Python_Classes\virtualExample\venv\Scripts\python.exe" "C:/My Data/PythonPractice/pynative/exercise_11-15.py"
* * * * *
* * * *
* * *
* *
*
"""
for j in range(5,0,-1):
    # for i in range(1,6):
    print('* '* j)
print()







"""
Question 13: Print multiplication table form 1 to 10
Expected Output:

1  2 3 4 5 6 7 8 9 10
2  4 6 8 10 12 14 16 18 20
3  6 9 12 15 18 21 24 27 30
4  8 12 16 20 24 28 32 36 40
5  10 15 20 25 30 35 40 45 50
6  12 18 24 30 36 42 48 54 60
7  14 21 28 35 42 49 56 63 70
8  16 24 32 40 48 56 64 72 80
9  18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100

"""
print("Multiplication table....")
for j in range(1,11):
    for i in range(1,11):
        print(j * i ,end=" ")

    print()


"""
    Question 12: Calculate income tax for the given income by adhering to the below rules
    Taxable Income	Rate (%)
First $10,000	0
Next $10,000	10
The remaining	20

Expected Output:
For example, suppose that the taxable income is $45000 the income tax payable is
$10000*0% + $10000*10%  + $25000*20% = $6000.
"""
income=int(input("Enter the income :"))
taxpayable=0
if income <=10000:
    taxpayable=0
elif income <= 20000:
    taxpayable=(income-10000) * 10/100
else:
    taxpayable=0

    taxpayable= 10000 * 10/100

    taxpayable=taxpayable+(income - 20000)* 20/100

print("Total tax to pay is", taxpayable)




"""
Question 11: Write a code to extract each digit from an integer, in the reverse order
Expected Output:

For example, if the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

"""
digit=int(input("Enter the digit : "))
print("The given number is :",digit)

while digit>0:
    num=digit%10

    digit= digit // 10

    print(num, end=" ")
#
# str_digit=str(digit)
#
# rev_str_digit=str_digit[::-1]
# nstr=rev_str_digit.partition(" ")
# print(rev_str_digit)
# print(nstr)

# rev_digit=int(rev_str_digit)
# print(rev_digit)

