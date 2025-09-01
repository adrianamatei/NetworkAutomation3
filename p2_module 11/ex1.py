# sa configuram doua interfete diferite pe acelasi device cu ip uri diferite folosind thread-uri, IOU1
import threading
from lib.connectors.telnet_module_11 import TelnetConnection
import threading
import asyncio
from lib.connectors.telnet_module_11 import TelnetConnection  # clasa ta TelnetConnection

HOST = '92.81.55.146'
PORT = 5120

lock = threading.Lock()

def configure_thread(interface, ip):
    async def job():
        conn = TelnetConnection(HOST, PORT)
        await conn.connect()

        await conn.configure(interface, ip)
    asyncio.run(job())

interfaces = [
    ("eth0/2", "192.168.202.1"),
    ("eth0/1", "192.168.201.1")
]


threads = []
for iface, ip in interfaces:
    t = threading.Thread(target=configure_thread, args=(iface, ip))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Toate interfețele configurate pe IOU1")
