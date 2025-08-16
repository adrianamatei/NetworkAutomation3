import asyncio
import telnetlib3

HOST = '92.81.55.146'
PORT = 5109

async def get_interface_ips(host, port):
    ethernet_ports = [f"Ethernet{slot}/{num}" for slot in range(0, 2) for num in range(0, 4)]
    serial_ports = [f"Serial{slot}/{num}" for slot in range(0, 2) for num in range(0, 2)]
    all_ports = ethernet_ports + serial_ports

    reader, writer = await telnetlib3.open_connection(host, port)
    writer.write('\n')

    async def read_until_prompt(reader, writer, prompt=b'IOU1#'):
        output = b""
        while True:
            chunk = await reader.read(1024)
            if not chunk:
                break
            output += chunk

            if b"--More--" in chunk:
                writer.write("\n")
                await asyncio.sleep(0.1)

            if prompt in chunk:
                break
        return output

    for interface in all_ports:
        writer.write(f"show int {interface}\n")
        output = await read_until_prompt(reader, writer)
        decoded = output.decode()
        ip_found = False

        for line in decoded.splitlines():
            if "Internet address is" in line:
                ip = line.split()[-1]
                print(f"{interface} has IP address: {ip}")
                ip_found = True
                break

        if not ip_found:
            print(f"{interface} has no IP address")

    writer.close()
    await writer.wait_closed()

# Run the function
asyncio.run(get_interface_ips(HOST, PORT))
