class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg=arg
class TooOldException(Exception):
    def __init__(self, arg):
        self.msg=arg


if __name__ == "__main__":
        age=int(input("Enter the age:"))
        if age>60:
                raise TooYoungException("Plz wait some time you will get best match soon")
        elif age<18:
                 raise TooOldException("Your age already closed marriege age... no chance of getting marrige")
        else:
            print("You will get match details soon by email !!!!")        
