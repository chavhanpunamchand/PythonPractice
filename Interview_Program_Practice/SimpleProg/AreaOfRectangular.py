'''
Program to calculate the area of the rectangle
formula:-
         A=WxH

'''
def AreaOfRect(w,h):
    if w <= 0:
        return "Enter A should be positive number"

    elif h <=0:
        return "Enter B should be positive number"

    return "Area of rectangle is:",w*h
flag=True
while flag:
    try:
        w=int(input("Enter the width of rectangle: "))

        h=int(input("Enter the height of rectangle: "))

    except:
        print("Enter proper number :")
    else:
        print(AreaOfRect(w,h))

    y=input('Do you want to continue:(y/yes): ')
    y.lower()
    if y=="y" or y=="yes":
        flag=True
    else:
        flag=False

