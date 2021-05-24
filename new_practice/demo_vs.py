
def decor(name_check):
    def inner(name):
        if name=="Punamchand":
            print("Hello Punamchand")
        else:
            return name_check(name)   
      
    return inner



@decor
def name_check(name):
    print("Hello "+ name +" You are a guest")


name=input("Enter the name : ")

resp=name_check(name)
# print(resp)