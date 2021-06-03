user_input=input("enter the num check palindrome or not: ")

temp=user_input
if temp == user_input[::-1]:
    print(" Palindrome ")

else:
    print("Not palindrome")
