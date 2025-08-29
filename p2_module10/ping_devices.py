#ping devices when config is done
#trebuie sa asteptam dupa device uri sa aiba configuratia facuta si apoi sa dam ping odata ce setup ul este facut
#sa generam un q care sa spuna utilizatorului cand poate merge sa verifice un anumit device
#q va rula pana cand dam ping la toate device urile printr un singur consumer
#functia care va popula q si una care va da ping prin subprocess
#trebuie sa i punem sa astepte un anumit timp

import asyncio
import os
from multiprocessing import Process, Queue
from lib.connectors.telnet_con import TelnetConnection
import subprocess

HOST = '92.81.55.146'
PORTS = [5120, 5029]

PORTS_IPS = [
    ("Ethernet0/0",        "192.168.200.3 255.255.255.0"),
    ("GigabitEthernet0/0", "192.168.200.4 255.255.255.0"),
]

CONNS: list[TelnetConnection] = []

for port in PORTS:
    CONNS.append(TelnetConnection(HOST, port))

async def configure_all(queue: Queue):
    await asyncio.gather(*(con.connect() for con in CONNS))
    await asyncio.gather(*(con.configure(iface, ip, completed=queue) for con, (iface, ip) in zip(CONNS, PORTS_IPS)))
    await asyncio.gather(*(con.close() for con in CONNS))

def ping_device(ip: str):
    print(f"{os.getpid()} Pinging {ip} ")
    subprocess.run(['ping', ip, '-c', '2'])

def consumer(queue: Queue):
    while not queue.empty():
        msg = queue.get()
        print("Got from queue:", msg)

        ip = msg.split("-")[-1].strip().split()[0]
        ping_device(ip)
    print(f"Consumer {os.getpid()} done")


if __name__ == "__main__":
    q = Queue()
    asyncio.run(configure_all(q))
    p1 = Process(target=consumer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()