
class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg

age=int(input("Enter the age: ")) #
if age>60:
    raise TooOldException("Your age alrady crosses the marrige age no change of getting marrige")
elif age<18:
    raise TooYoungException("please wait for some time you will get best match")

else:
    print("you will get marrige details soon by mail")