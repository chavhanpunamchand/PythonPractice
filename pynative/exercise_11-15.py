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

