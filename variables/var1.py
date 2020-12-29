'''
1.Global
2.Local

'''
#check the git status and confedential



a=10
b=5000
def outerfun(num):
    # global b
    b=1000000
    # print(a)
    print("out local var ",b)
    print("global....",globals()['b'])
    # outerfun(10)

# def f2():
#      print(a)
#      print(" f2 local var ",b)

outerfun(120)
# f2()
