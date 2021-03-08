"""
Check if all item in the following tuple are the same
"""

def check(sample_tuple):
    return all(i== sample_tuple[0] for i in sample_tuple)

tuple1=(45,45,45,45)

print(check(tuple1))


import sys
sys.exit(0)

"""
Sort a tuple of tuples by 2nd item
"""
tuple1=(('a',23),('b',37),('c',11),('d',29))
tuple1=tuple(sorted(list(tuple1),key=lambda x:x[1]))
print(tuple1)


"""
copy element 44 and 55 from the following tuple into a new tuple
"""
tuple1=(11,22,33,44,55,66)
tuple2=tuple1[3:-1]
print(tuple2)



import sys
sys.exit(0)
"""
unpack the following tuple into 4 variables
"""
atuple=(10,20,30,40)
a,b,c,d=atuple
print(a)
print(b)
print(c)
print(d)