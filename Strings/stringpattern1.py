"""
input: "a4b3c2"
output:aaaabbbcc
"""

input="aa4b3c2dfe"
output=""
for ch in input:
    if ch.isalpha():
        output=output + ch
        x=ch
    else:
        d=int(ch)
        output=output + x * (d-1)

print(output)


