
def add(**kwargs):
    c=kwargs['a']-kwargs['b']
    return c


# result=add(90,10) position as arg
# result=add(b=90,a=10)# keyword
# result=add(a=10)# default
result=add(a=10,b=90)# default
print(result)






import sys
sys.exit(0)

def subt(**kwargs):
    i=0
    while i <=len(kwargs):
        a=kwargs['a']
        b=kwargs['b']
        i=i+1
        return a-b




# result=subt(10,2)  #position
# result=subt(b=10,a=2)  #keyword as args
# result=subt(a=10)  #defult as args
result=subt(a=10,b=2)  #variable lenght as args
print(result)




import sys
sys.exit(0)


def add(a,b):
    c=a+b
    return c,a,b


result,a=add(10,20)
print(result)
print(a)
# print(b)





def wish(name):
    print("Hi good morning",name)



wish("Punamchand")

