num=int(input("enter the number to check palindrome or not: "))

temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if rev==temp:
    print("Palindrone")
else:
    print("Not palindrome....")
