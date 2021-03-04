"""
from given string replace each punctuation with #
"""
from string import punctuation
str1="/*Jon is @developer &musician"
print("Original string is ",str1)

replace_char='#'

for char in punctuation:
    str1=str1.replace(char,replace_char)

print("The strings after replacement :",str1)




import sys
sys.exit(0)
import re
str1="/*Jon is @developer &musician"
print("Original string is ",str1)
str2=re.sub('[^\w\s]','',str1)
print("New string is ",str2)

""" remove special symbol/punctuation from a given string """
from string import punctuation
str1="/*Jon is @developer &musician"
print("Original string is ",str1)
#use translate function of a string
#and maketrans function of str class

new_str=str1.translate(str.maketrans("","",punctuation))

print("New string is",new_str)


"""
remove empty string from list of strings
"""
str_list = ["Punamchand", "", "Satish", "Rupesh", "Shrikant", "", "", "Vivek"]
print("Original list of string :", str_list)
new_list = list(filter(None, str_list))
print("After removing empty string :")
print(new_list)
