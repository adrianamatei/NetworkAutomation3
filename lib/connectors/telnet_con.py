import asyncio
import time
import re

import telnetlib3

HOST = '92.81.55.146'
PORT = 5120  # replace with yours

class TelnetConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        return self

    async def connect(self):
        self.reader, self.writer = await telnetlib3.open_connection(self.host, self.port)

    def print_info(self):
        print('Reader: {}'.format(self.reader))
        print('Writer: {}'.format(self.writer))

    async def readuntil(self, separator: str):
        response = await self.reader.readuntil(separator.encode())
        return response.decode()

    async def read(self, n: int):
        return await self.reader.read(n)

    def write(self, data: str):
        self.writer.write(data)
    async def configure(self):

        pass
    '''async def configure(self):
        self.write('\n')
        await asyncio.sleep(1)
        result = await self.read(1000)
        print(f"Name: {result}")
        pattern = re.compile(r"^(\w+)#|^(\w+)>", re.M)

        match=pattern.search(result)
        if not match:
            print("Nu a fost detectat un prompt corect")
            return
        if match.group(1):
            hostname_device = match.group(1)
        else:
            hostname_device = match.group(2)
        print(f"Hostname: {hostname_device}")
        if hostname_device == 'IOU1':
            print("Se configureaza device ul IOU1")
            self.write("conf t\n")
            await asyncio.sleep(1)
            self.write("int e0/0\n")
            await asyncio.sleep(1)
            self.write("ip address 192.168.200.10 255.255.255.0\n")
            await asyncio.sleep(1)
            self.write("no shutdown\n")
        elif hostname_device == 'Router':
            print("Se configureaza device ul Cisco CSR")
            self.write("enable\n")
            await asyncio.sleep(1)
            self.write("conf t\n")
            await asyncio.sleep(1)
            self.write("int g0/0\n")
            await asyncio.sleep(1)
            self.write("ip address 192.168.200.20 255.255.255.0\n")
            await asyncio.sleep(1)
            self.write("no shutdown\n")

        await asyncio.sleep(1)
        self.write("end\n")
        await asyncio.sleep(1)
        self.write("write memory\n")
        await asyncio.sleep(1)'''

    async def close(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.write('\n')

if __name__ == '__main__':
    conn = TelnetConnection(HOST, PORT)

    async def main():
        await conn.connect()
        conn.write('\n')
        await conn.readuntil('\n')
        conn.print_info()
    asyncio.run(main())

    # conn.print_info()

    # asyncio.run(conn.connect_to_device())
    # conn.print_info()

    # with TelnetConnection(HOST, PORT) as conn:
    #     asyncio.run(conn.connect_to_device())
    #     conn.print_info()


'''
async def configure(self):
        self.write('\n')
        await asyncio.sleep(1)
        result = await self.read(1000)
        print(f"Name: {result}")

        pattern = re.compile(r"^(\w+)#|^(\w+)>", re.M)
        match = pattern.search(result)
        if not match:
            print("Nu a fost detectat un prompt corect")
            return

        if match.group(1):
            hostname_device = match.group(1)
        else:
            hostname_device = match.group(2)
        print(f"Hostname: {hostname_device}")

        print(f"Acum poți introduce comenzile pentru {hostname_device}. Scrie 'quit' pentru a termina.")
        while True:
            cmd = input(f"{hostname_device}> ")
            if cmd.lower() in ('quit',):
                print(f"Ieșire din modul interactiv pentru {hostname_device}.")
                break
            self.write(cmd + '\n')
            await asyncio.sleep(0.5)
            response = await self.read(1000)
            print(response)

        self.write("end\n")
        await asyncio.sleep(0.5)
        self.write("write memory\n")
        await asyncio.sleep(1)
        print(f"Configurarea finală pentru {hostname_device} a fost salvată.")
'''