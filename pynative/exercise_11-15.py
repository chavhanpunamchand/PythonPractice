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




import sys
sys.exit(0)
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

