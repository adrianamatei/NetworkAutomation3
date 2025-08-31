import asyncio
import time
import re
from queue import Queue

import telnetlib3

HOST = '92.81.55.146'
PORT = 5120  # replace with yours
PORT_DEVICE_MAP = {
    5120: "IOU1",
    5121: "CiscoIOSv"
}

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

    async def detect_prompt(self):
        self.write('\n')
        await asyncio.sleep(1)
        result = await self.read(1000)
        match = re.search(r'([\w\-\.:]+)(>|#)', result)
        if match:
            return match.group(0)
        return None

    #la tema3 cred ca am nevoie de varinata configure fara Queue
    async def configure(self, filename="output.txt"):
        device_name = PORT_DEVICE_MAP[self.port]  # port -> nume device
        prompt = await self.detect_prompt()

        if prompt.endswith('>'):
            self.write('enable\n')
            prompt = await self.detect_prompt()

        self.write('show running-config\n')
        running_config = await self.readuntil(prompt)

        with open(filename, "w") as f:
            f.write(running_config)

        print(f"Saved running-config for {device_name} in {filename}")

    async def restore_config(self, commands):
        prompt = await self.detect_prompt()
        if prompt.endswith('>'):
            self.write('enable\n')
            prompt = await self.detect_prompt()

        self.write('conf t\n')
        await self.readuntil('(config)#')


        for cmd in commands:
            self.write(cmd + '\n')
            await self.readuntil('(config)#')

        self.write('end\n')
        await self.readuntil(prompt)
        print(f"Restored configuration on {PORT_DEVICE_MAP[self.port]}")

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