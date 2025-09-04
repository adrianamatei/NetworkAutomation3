import threading
import time

sem=threading.Semaphore(2)
def worker(i):
    with sem:
        print(f"Thread {i} entered ")
        time.sleep(2)
        print(f"Thread {i} exiting ")
for i in range(5):
    threading.Thread(target=worker,args=(i,)).start()
