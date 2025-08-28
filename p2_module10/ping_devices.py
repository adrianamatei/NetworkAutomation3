#ping devices when config is done
#trebuie sa asteptam dupa device uri sa aiba configuratia facuta si apoi sa dam ping odata ce setup ul este facut
#sa generam un q care sa spuna utilizatorului cand poate merge sa verifice un anumit device
#q va rula pana cand dam ping la toate device urile printr un singur consumer
#functia care va popula q si una care va da ping prin subprocess
#trebuie sa i punem sa astepte un anumit timp

import time
import os
from lib.connectors.telnet_con import TelnetConnection
import asyncio
from multiprocessing import Process, Queue
import subprocess



HOSTS = [('92.81.55.146', 5120), ('92.81.55.146', 5029)]
CONNS = [TelnetConnection(host, port) for host, port in HOSTS]

async def producer(q, connections):
    await asyncio.gather(*(con.connect() for con in connections))
    for con in connections:
        await con.configure(completed=q)
    await asyncio.gather(*(con.close() for con in connections))
    q.put(None)


def consumer(q):
    while True:
        ip = q.get()
        if ip is None:
            break
        print(f"Pinging {ip}...")
        try:
            subprocess.run(["ping", ip], check=True, timeout=5)
            print(f"{ip} este reachable")
        except subprocess.CalledProcessError:
            print(f"{ip} nu răspunde")
    print(f"Consumer {os.getpid()} terminat")



if __name__ == "__main__":
    q = Queue()
    p_consumer = Process(target=consumer, args=(q,))
    p_consumer.start()
    asyncio.run(producer(q, CONNS))
    p_consumer.join()
