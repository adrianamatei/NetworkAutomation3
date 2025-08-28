#ping devices when config is done
#trebuie sa asteptam dupa device uri sa aiba configuratia facuta si apoi sa dam ping odata ce setup ul este facut
#sa generam un q care sa spuna utilizatorului cand poate merge sa verifice un anumit device
#q va rula pana cand dam ping la toate device urile printr un singur consumer
#functia care va popula q si una care va da ping prin subprocess
#trebuie sa i punem sa astepte un anumit timp
import time
import os
from multiprocessing import Process, Queue

def producer(q):
    for i in range(5):
        time.sleep(1)
        q.put(i)

def consumer(q):
    while not q.empty():
        item = q.get()
        print("Consuming: ",item)
        time.sleep(2) #determines consumtion rate
        print("Consumed:", item)
    print(f"Consumer {os.getpid()} done")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p3 = Process(target=consumer, args=(q,))
    p1.start()
    time.sleep(3)
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()