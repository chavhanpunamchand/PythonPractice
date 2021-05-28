"""
Reverse string without using any function
"""

def reverse_str(str1):
        i=len(str1)-1
        output=""
        while i>=0:
            output=output+str1[i]
            i=i-1
        return output

str1="Punamchand"
output=reverse_str(str1)
print(output)