try:
    print("Outer try block")
    print(10/0)
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("Outer except block")

finally:
    print("Outer finally block")                    