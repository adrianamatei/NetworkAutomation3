#connect to all devices in list
#call function to configure management interface
#close all connections
import asyncio

from lib.connectors.telnet_con import TelnetConnection

PORT=[5120,5014]
CONNS:list[TelnetConnection] = []
HOST = '92.81.55.146'

for port in PORT:
    CONNS.append(
        TelnetConnection(HOST,port)
    )
#sau functii diferite

async def main():
        await asyncio.gather(*(con.connect() for con in CONNS))
        await asyncio.gather(*(con.configure() for con in CONNS))

        await asyncio.gather(*(con.close() for con in CONNS))


asyncio.run(main())
