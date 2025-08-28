import multiprocessing as mp
import os
import time


def worker(name):
    time.sleep(1)
    print(f'Worker {name} running in process id:{os.getpid()} ')
    time.sleep(1)
    print(f'Worker {name} exiting ')


if __name__=="__main__":
    p1=mp.Process(target=worker,args=('A',))
    p2=mp.Process(target=worker,args=('B',))
    p1.start() # start este cel care porneste procesul nostru
    p2.start()
    p1.join()# join aduce mesajele inapoi in script
    p2.join()#vreau sa astept dupa cele doua procese ca sa incheie ele executia dupa care sa merg mai departe
    print("Both processes finished")

