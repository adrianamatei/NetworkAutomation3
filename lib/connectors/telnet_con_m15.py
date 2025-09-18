import asyncio
from os import write
from queue import Queue

import telnetlib3

HOST = '92.81.55.146'
PORT = 5120 # replace with yours

class TelnetConnection:
    def _init_(self, host, port):
        self.host = host
        self.port = port

    def _enter_(self):
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
        self.writer.write(data + '\n')

    def _exit_(self, exc_type, exc_val, exc_tb):
        self.write('\n')

    async def execute_commands(self, command: list, prompt: str):
        for cmd in command:
            self.write(cmd + '\n')
            await self.readuntil(prompt)

if __name__ == '__main__':
    conn = TelnetConnection(HOST, PORT)

    async def main():
        await conn.connect()
        conn.write('\n')
        await conn.readuntil('\n')
        conn.print_info()
    asyncio.run(main())