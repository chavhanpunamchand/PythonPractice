"""
Remove items from set1 that are not common to both set1 and set2
"""
set1={10,20,30,40,50}
set2={30,40,50,60,70}

set1.intersection_update(set2)
print(set1)




import sys
sys.exit(0)
""" 
Determine whether or not the following two sets have any elements in common.
if yes display the common elements
"""
set1={10,20,30,40,50}
set2={60,70,80,90,10}

if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))


"""
Remove 10,20,30 elements from a following set at once
"""
set1={10,20,30,40,50}

set1.difference_update({10,20,30})
print(set1)