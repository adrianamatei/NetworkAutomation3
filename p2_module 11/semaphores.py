
import threading, time

sem = threading.Semaphore(2)  # max 2 threads allowed at once

def worker(i):
     with sem:
         print(f"Thread {i} entered")
         time.sleep(2)
         print(f"Thread {i} exiting")

for i in range(5):
     threading.Thread(target=worker, args=(i,)).start()