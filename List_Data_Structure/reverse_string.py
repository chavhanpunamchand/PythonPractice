def convert(s):
    new=""
    for x in s:
        new+=x
        #print()   
    return new    


s="Punamchand is scientiest"
l=s.split()
d=l[::-1]
print(d)
print(" ".join(convert(d)))