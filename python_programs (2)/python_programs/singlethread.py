
import random
values = []     # 100 numbers -->

import time
def generate_num():
    num = random.randint(1,1000)
    values.append(num)


import threading

def main_task():
    while True:
        if len(values)==10000000:
            break
        generate_num()


if __name__ == '__main__':      # single thread..
    start = time.time()
    main_task()
    end = time.time()
    print("Total Time Required : ",end-start)
    #print('Here is values : ' ,values)
