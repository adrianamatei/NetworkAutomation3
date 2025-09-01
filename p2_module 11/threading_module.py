import threading
import time
import random

global_var=[]

def worker(name):
    print(f'Thread {name} starting ')
    sleep_time=random.randint(1,5)
    time.sleep(sleep_time)
    global_var.append(sleep_time)
    print(f'Thread {name} finished ')



t1=threading.Thread(target=worker,args=('A',))
t2=threading.Thread(target=worker,args=('B',))
t1.start()
t2.start()
global_var.append(random.randint(1,5))
t1.join()
t2.join()
print("Both threads finished")
print(global_var)