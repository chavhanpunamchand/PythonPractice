def group_by_owners(files):
    print(type(files))
    list1=[]
    list2=[]
    dict1={}
    for k,v in files.items():
        print(k,v)
        if v not in dict1.keys():
            list1.append(k)
            dict1[v] = {}

        else:
            list2.append(k)

    return dict1

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))



import sys
sys.exit(0)
def unique_names(names1, names2):
    new_name1=set(names1)
    new_name2=set(names2)
    return new_name1.union(new_name2)


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia


import sys
sys.exit(0)
class MathUtils:

    @staticmethod
    def average(a, b):
        return a + b / 2

print(round(MathUtils.average(2, 1),2))