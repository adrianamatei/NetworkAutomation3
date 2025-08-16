'''# get configuration (running/startup config) from IOU1 and save to file
import asyncio
import telnetlib3
import time

HOST = '92.81.55.146'
PORT = 5109


async def connect_and_save_startup_config(host, port):
    try:
        reader, writer = await telnetlib3.open_connection(host, port)
        writer.write('\n')
        response = await asyncio.wait_for(reader.read(200), timeout=1)
        print(response)

        if 'IOU1#' in response:
            writer.write('show startup-config\n')
            output_bytes = await reader.readuntil(b'IOU1#')
            output = output_bytes.decode()
            try:
                with open("startup_config.txt", "w") as file:
                    file.write(output)
                print("Startup-config salvat cu succes !")
            except Exception as e:
                print(f"Eroare la scrierea fișierului: {e}")
                time.sleep(15)

            try:
                with open("startup_config.txt", "r") as file:
                    response_file = file.read()
                print(response_file)
            except Exception as e:
                print(f"Eroare la citirea fișierului: {e}")
                time.sleep(15)

        writer.close()
        await writer.wait_closed()

    except Exception as e:
        print(f"Eroare la conexiunea Telnet: {e}")
        time.sleep(15)

asyncio.run(connect_and_save_startup_config(HOST, PORT))
'''
# get full configuration (running/startup config) from IOU1 and save to file
# get full configuration (running/startup config) from IOU1 and save to file

import asyncio
import telnetlib3
import time

HOST = '92.81.55.146'
PORT = 5109


async def connect_and_save_startup_config(host, port):

        reader, writer = await telnetlib3.open_connection(host, port)
        writer.write('\n')
        #response = await asyncio.wait_for(reader.read(200), timeout=1)
        response=await reader.redundant(b"IOU1#")


        if 'IOU1#' in response:
            writer.write('show startup-config\n')
            response=await reader.readuntil(b'--More--')
            while "--More--" in await reader.read(b"--More--"):
                if "IOU#" in response.decode():
                    writer.write(' ')
                    response=await reader.readuntil(b'IOU1#')
                decoded=response.decode()
                print(decoded)
        with open("running-config.txt","w") as file:
            for line in decoded.splitlines():
                if "--More--" in line:
                    file.write(line+"\n")
asyncio.run(connect_and_save_startup_config(HOST, PORT))
