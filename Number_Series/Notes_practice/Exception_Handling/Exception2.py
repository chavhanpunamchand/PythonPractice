
try:
    x=int(input("Enter the A number :"))
    y=int(input("Enter the B number :"))
    z=x/y
    print(z)
except (ValueError,ArithmeticError,ZeroDivisionError,) as msg:
    print(msg)
    print("Enter the proper number according to formate")
else:
    print("Print this block of code run, if not occure the exception")

finally:
    print("closed all resourses")        
