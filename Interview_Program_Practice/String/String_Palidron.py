'''
s="Radar"
s1=s.upper()
s2=s.lower()
print(s1)
print(s2)

import os
exit(0)


'''

#function for check given string palidrom or not
def isPalindrome(s):
    # revS=s.upper()

    # return s==revS
    return s==s[::-1]





#give the string
s="Punamchand"
checkP=isPalindrome(s)
if checkP:
    print("yes")
else:
    print("No")
