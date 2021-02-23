import re
s=input("Enter the vehicle Registration Number: ")
m=re.fullmatch('MH[01234][0-9][A-Z]{2}\d{4}',s)
if m!=None:
    print("Valid vehicle Registration number ")

else:
    print("Invalid registration number")
