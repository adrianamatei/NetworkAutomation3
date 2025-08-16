import asyncio

import telnetlib3

import telnetlib3
HOST='92.81.55.146'
PORT=5109
async def connect_to_device(host, port):
    reader,writer=await telnetlib3.open_connection(host,port)
    writer.write('\n') #asa trimit o comanda
    response=await asyncio.wait_for(reader.read(200),timeout=1)
    print(response)
    if 'IOU1#' in response:
        #writer.write("show interfaces Ethernet1/1\n")
        #response=await reader.readuntil(b"IOU1#")
        #verificam daca avem ip address pe interfata aceea
        #print(type(response))

        for item1 in range(0, 2):
            for item2 in range(0, 4):
                interface = f"Ethernet{item1}/{item2}"
                writer.write(f"show interfaces {interface}\n")
                output_bytes = await reader.readuntil(b"IOU1#")
                output = output_bytes.decode()
                found = False
                for line in output.splitlines():
                    if "Internet address is" in line:
                        print(f" {interface} are configurata adresa IP :", line.strip())
                        found = True

                if not found:
                    print(f" {interface} nu are configurata adresa IP !")


asyncio.run(connect_to_device(HOST,PORT))

'''
VARIANTA ELVIS
async def connect_to_device(host, port):
    reader, writer = await telnetlib3.open_connection(host, port)
    writer.write('\n')
    response = await reader.readuntil(b"IOU1#")
    # response = await asyncio.wait_for(reader.read(200), timeout=2)
    print(response)
    for port in range(0, 2):
        for port_number in range(0, 4):
            writer.write(f"show int e{port}/{port_number}\n\t")
            response = await reader.readuntil(b"IOU1#")
            for line in response.splitlines():
                if b"Internet address is" in line:
                    ip=line.decode().split()[-1]
                    #print(f"e{port}/{port_number}:{line.strip()}")
                    print(ip)
'''
'''
VARIANTA BOGDAN
import asyncio

import telnetlib3

HOST = "92.81.55.146"
PORT = 5029

async def connect_to_device(host, port):
    reader, writer = await telnetlib3.open_connection(host, port)
    writer.write('\n')
    response = await reader.readuntil(b"IOU1#")
    # response = await asyncio.wait_for(reader.read(200), timeout = 1)
    print(response)
    if "IOU1#" in response.decode():
        writer.write('sh ip int br\n')
        response = await reader.readuntil(b"IOU1#")
        decoded = response.decode()
        for line in decoded.splitlines():
            if "Ethernet" in line or "Serial" in line:
                parts = line.split()
                if parts[1] != "unassigned":
                    print(f"{parts[0]} has an IP address of : {parts[1]}")



asyncio.run(connect_to_device(HOST, PORT))



 
'''