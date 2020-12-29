
def addition(n1,n2):
    return n1+n2

#assert addition(10,20)==30      # addition ch output expected -- 30 --> actual and expected ->



#decorator --> fun-->
#decorater concept is based on closures -- and closure is based on inner functions -->
def outer(fun):
    def inner(param):   #
        fun(param)
    return inner


def outer(n1):
    def inner(n2):
        print('inside inner')

    return inner

#every outer call -- returns -- new inner instance -- will associate outer params-- inside inner -->
x1  = outer()
x2 = outer()
x3 = outer()



del x1
del x2
del x3

# outer -call --> yes -->
# call i call to inner -- x1,x2,x3 --> we can create new inner --> outer -- new inner

#del outer       # can i call to the inner -->

#we can call to inner ---> 3 -->
# can we create new inner instance --> NO --> in order to create inner-- we need outer ref-->



x1()    # can -- outer cha data inner la milel ka ---> Yes

#x4 = outer()    #not possible -- outer cha ref-- deleted ->






#function -- is an object python --> at any point of time-- property -- add/remove -->

def outer(num1):        #num1 -- local --> outer--> kadhi paryant--> outer execution
    def inner(num2):
        result = num1 + num2    # num1 access ??? --> closures--> associate the outer function data --> to inner functions->
        print(result)
    return inner

x1 = outer(10)  # x holds inner ref -->      line7- outer execuction --> num1 -- vanish --> # x1 : num1:10
x2 = outer(22)                                                                              #x1  : num1:20
#another logic

x1(20)  #num1--10+20         # -> inner will be called     --> i can access it here -->
x2(20)  #num1-22+20





def outer(p1):      #p1 --> params-- by default --> p1 -- existance --> till outer gets completed
    num1 = 10           # 10
    num2 = p1           #100

#x = outer(100)  #  at the time of execution -- num1:10,num2:100 x:nasel ->after fun execution -->num1--nasel - num2 --nasel -- p1 -- nasel ---> x- None
#y = outer(200) #  at the time of execution -- num1:10,num2:100 x:nasel ->after fun execution -->num1--nasel - num2 --nasel -- p1 -- nasel ---> y- None

