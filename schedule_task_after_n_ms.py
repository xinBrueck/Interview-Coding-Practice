###This function is to define a schedule that
###take a function f and time t in ms
###run the function after t ms

#####From the solution  Daily Coding Problem########
#####we probably want to implement a thread to run the function
#####instead of running the funtion in the scheduler
#####since the function can run arbitrarily long!

import threading
import time

def f():
    print("Start the function f!")
    return

def scheduler(f, t):
    time.sleep(t/1000)
    f()
    return

def scheduler_v2(f, t):  ###Inspired from Daily Coding Problem###
    def sleep_t_ms():
        time.sleep(t/1000)
        print(time.time())
        f()

    th = threading.Thread(target = sleep_t_ms)
    th.start()
    return

####test
print(time.time())
scheduler(f, 1000)
print(time.time())
scheduler_v2(f, 4000)
