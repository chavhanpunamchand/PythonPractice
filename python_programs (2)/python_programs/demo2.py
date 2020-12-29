
import threading
import time

values = []
def task1():
    for item in range(1,11):
        time.sleep(1)
        values.append(item) # 1 2 3 4  - 10 --> list madhe
        print(threading.current_thread().getName(),": ",item)
    print(threading.current_thread().getName(), " Completed ")

def task2():
    for item in range(101,111):
        time.sleep(1)
        values.append(item) # 101 102 --> 110
        print(threading.current_thread().getName(),": ",item)
    print(threading.current_thread().getName(), " Completed ")


if __name__ == '__main__':

    # 3 --> mainthread -->t1t2 start --> t1  [1,10]         t2 - [1,10] --> 3 thread stack --> whichever having less work--
    t1 = threading.Thread(target=task1, name="T1")  # task1()  -->os will decide --> ref detoy -- cal os will
    t2 = threading.Thread(target=task2, name="T2")  # task2() --> os will decide
    t1.start()
    t2.start()

    #main chya context madhe t1 join --> t1 will complete first and then main
    t1.join()
    t2.join()

    print('main completed',values)

    # start --> main -->    t1 t2
            #   complete --> t1 or t2 -->
                              #if t1 trch main
    # main or t2 --> last

    import sys
    sys.exit(0)
    x = task2()     # direct calling
    y = task2       # ref assignement-- at any point of time u say -- y() --> will call

    t1 =threading.Thread(target=task1(),name="T1")      #task1()
    t2 = threading.Thread(target=task2(), name="T2")      #task2()

    t1 =threading.Thread(target=task1,name="T1")      #task1()  -->os will decide --> ref detoy -- cal os will
    t2 = threading.Thread(target=task2, name="T2")      #task2() --> os will decide



                        #mainthread
#normal thread -->          t1                      t1  --> 10
#daemon thread -->          t2                      t2(d)-->20
                    #python process (t1 and t2 not gets completed)----------------


import threading

#active_count --> no of threads --> running wale
#current_thread --> name,id,pro-->

#def start(self) -> None: ...   --> register ur thread in thread scheduler and assign task -->
#def run(self) -> None: ...      --> work/task for the thread
#def join(self, timeout: Optional[float] = ...) ->  --> context wala will join later
                                                #maincontext    x1.join()   --> x1 will complete first and then context wala
#def getName(self) -> str: ...          # to retrive thread name
#def setName(self, name: str) -> None: ...  # to modify thread name
#def is_alive(self) -> bool: ...
#def isAlive(self) -> bool: ...         #currenly running ahe ka
#def isDaemon(self) -> bool: ...
#def setDaemon(self, daemonic: bool) -> None: ...


#multiprogramming/processing/tasking/threading
# django--> session- start-- 12.30pm


#Lock
#RLock
#Event
#Condition
#Semaphore
#BoundedSemaphore
#Barrier
#Timer

#deadlock
#starvation
#race condition
#thread safe
#sync
#join/yield
