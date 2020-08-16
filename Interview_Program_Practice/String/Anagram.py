str1=input("Enter the first string :")
str2=input("Enter the second string :")

if len(str1)==len(str2):
    if sorted(str1)==sorted(str2):
        print("The given string is Anagram...")
    else:
        print("Given string is not anagram...")
else:
    print("Given string is not anagram...")