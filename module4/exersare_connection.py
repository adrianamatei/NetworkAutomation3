import asyncio
import telnetlib3
import re
from datetime import datetime

HOST = '92.81.55.146'
PORT = 5041
PROMPT = b"IOU1#"

# Comenzile pe care vrei să le rulezi
COMENZI = [
    "show running-config",
    "show ip interface brief",
    "show version",
    "show ip route"
]

# Funcție pentru curățarea textului
def curata_output(output: str, comanda: str):
    return '\n'.join(
        line for line in output.splitlines()
        if '--More--' not in line
        and '\x08' not in line
        and comanda not in line
        and not re.match(r'^\s*$', line)
    ) + '\n'

# Citire până la prompt, cu gestionare --More--
async def citeste_pana_la_prompt(reader, writer, prompt=PROMPT):
    rezultat = b""
    while True:
        bucata = await reader.read(1024)
        if not bucata:
            break
        rezultat += bucata

        if b"--More--" in bucata:
            writer.write(" ")
            await asyncio.sleep(0.1)

        if prompt in bucata:
            break
    return rezultat

# Funcția principală
async def ruleaza_comenzi(host, port):
    reader, writer = await telnetlib3.open_connection(host, port)
    writer.write("\n")
    await reader.readuntil(PROMPT)

    for comanda in COMENZI:
        print(f"[INFO] Rulez comanda: {comanda}")
        writer.write(comanda + "\n")
        output_raw = await citeste_pana_la_prompt(reader, writer)
        output_curat = curata_output(output_raw.decode(errors="ignore"), comanda)

        # Nume fișier bazat pe comanda + timestamp
        nume_fisier = f"{comanda.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(nume_fisier, "w") as fisier:
            fisier.write(output_curat)
        print(f"[OK] Rezultatul salvat în {nume_fisier}")

    writer.close()
    await writer.wait_closed()

# Rulare script
asyncio.run(ruleaza_comenzi(HOST, PORT))
