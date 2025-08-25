#extract ip addr from ubuntu

import subprocess

'''
process = subprocess.Popen(["ip", "addr", "show"],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True)

stdout, stderr = process.communicate()
ip_addr = None
for line in stdout.splitlines():
    line = line.strip()
    if line.startswith("inet ") and not line.startswith("inet 127."):
        ip_addr = line.split()[1].split("/")[0]
        break

print("Adresa IP:", ip_addr)
'''
#O ALTA ABORDARE A PROBLEMEI, regex expression





