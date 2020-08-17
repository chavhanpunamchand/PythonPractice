'''
Sheena loves eating Apple and Mango . Her sister also loves eating Apple and Mango .

'''
def freq_Words():
    str=input("Enter a String :")
    ls=str.split()
    d={}

    for i in ls:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)

freq_Words()