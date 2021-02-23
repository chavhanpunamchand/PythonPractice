








import sys
sys.exit(0)
"""
print following pattern
1
1 2
1 2 3 4
1 2 3 4 5

"""

print("Number pattern")
last_num = 6
for i in range(1, last_num):
    for j in range(1, i + 1):
        print(j, end=" ")

    print(" ")
