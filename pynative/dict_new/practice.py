"""
create a new dictionary by extracting the following keys from he given dict
"""

sampleDict={"name":65,
            "age":25,
            "salary":8000,
            "city":1
            }
keys=["name","salary"] # fetch keys in dict
newDict={k: sampleDict[k] for k in keys}
keys_to_remove=["name","salary"] #remove keys
newDict={k: sampleDict[k] for k in sampleDict.keys() - keys_to_remove}
sampleDict['location']=sampleDict.pop('city')
sampleDict['salary']=15000
print(min(sampleDict, key=sampleDict.get))
print(sampleDict)





import sys
sys.exit(0)
""" merch two python dictionary into one"""
dict1={'Ten':10,'Twenty':20,'Thirty':30}
dic2={'Thirty':30,'fourty':40,'fifty':50}

dict3={**dict1,**dic2}
print(dict3)
dict1.update(dic2)
print(dict1)



"""
below two lists converted it into the dictionary
"""
keys=['Ten','Twenty','Thirty']
values=[10,20,30]

sample_dict= dict(zip(keys,values))
print(sample_dict)