
import random
values = []     # 100 numbers -->

import time
def generate_num():
    num = random.randint(1,1000)
    values.append(num)


import threading

def main_task():
    while True:
        if len(values)>=10000000:      # 10000 --> hoel            10001
            break
        generate_num()

    print(threading.current_thread().name +" completed")

if __name__ == '__main__':      # single thread..
    start = time.time()
    t1 = threading.Thread(target=main_task,name="T1")   # 8 10 --> complete
    t2 = threading.Thread(target=main_task, name="T2")  # 9 11
    t3 = threading.Thread(target=main_task, name="T3")  # 9 11
    t4 = threading.Thread(target=main_task, name="T4")  # 9 11
    #t4.setDaemon(True)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
                        #5 -- t1-t4 -- main
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    end = time.time()       # main will not complete till the time -t1t2t3t4
    print("Total Time Required : ",end-start)
    #print('Here is values : ' ,values)
