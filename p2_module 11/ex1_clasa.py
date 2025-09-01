# configure in different threads different interfaces on same IOU1 device
'''
#Varianta BOGDAN
import threading
import asyncio
from lib.connectors.telnet_con import TelnetConnection

HOST = "92.81.55.146"
PORT = 5120
lock = threading.Lock()


async def config_int(interface:str, ip:str):
    conn = TelnetConnection(HOST, PORT)
    await conn.connect()

    conn.write('\n')
    await conn.readuntil('#')
    conn.write('conf t\n')
    await conn.readuntil('(config)#')
    conn.write(f'int {interface}\n')
    await conn.readuntil('(config-if)#')
    conn.write(f'ip add {ip} 255.255.255.0\n')
    await conn.readuntil('(config-if)#')
    conn.write('no sh\n')
    await conn.readuntil('(config-if)#')
    conn.write('end\n')
    await conn.readuntil('#')


def config_threads(int, ip):
    with lock:
        asyncio.run(config_int(int, ip))


t1 = threading.Thread(target=config_threads, args=('e0/1', '192.168.201.1'))
t2 = threading.Thread(target=config_threads, args=('e0/2', '192.168.202.1'))
t1.start()
t2.start()
t1.join()
t2.join()'''

#VARIANTA SILVIU-trebuie sa o actualizez cu varianta de pe git
import asyncio, threading, telnetlib3

HOST, PORT = "92.81.55.146", 5186
IFACES = {
    "e0/1": "192.168.200.4 255.255.255.0",
    "e0/2": "192.168.200.5 255.255.255.0"
}


async def configure(iface, ip):
    r, w = await telnetlib3.open_connection(HOST, PORT)

    def send(cmd):
        w.write(cmd + "\r\n")

    async def wait():
        await r.readuntil(b"#")

    for cmd in ["", "conf t", f"int {iface}", f"ip address {ip}", "no shut", "end", "wr"]:
        send(cmd)
        await wait()
    print(f"[OK] {iface} -> {ip}")
    w.close()


def thr(iface, ip):
    asyncio.run(configure(iface, ip))


threads = [threading.Thread(target=thr, args=(i, ip)) for i, ip in IFACES.items()]
[t.start() for t in threads]
[t.join() for t in threads]






