""" given a nested list extend it with adding sub list ["h","i","j"] in a such a way that """

list1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
sublist=['h','i','j']

list1[2][1][2].extend(sublist)
print(list1)




import sys
sys.exit(0)
"""
given a python list, remove all occurrence of 20 from the list
"""
def remove_val(list1,val):
    return [value for value in list1 if value != val]


list1=[5,20,15,20,25,50,20]

removed_list=remove_val(list1,20)
print(removed_list)
