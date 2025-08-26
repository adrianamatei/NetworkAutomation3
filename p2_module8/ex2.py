#check the second interface has IP and if not, set IP
#ens4 e a doua interfata
import re

import subprocess
import re
import subprocess

# Obține ieșirea comenzii `ip addr show`
process = subprocess.Popen(
    ['ip', 'addr', 'show'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
std_out, std_err = process.communicate()

# Găsește toate interfețele și IP-urile lor
interfaces = re.findall(r'^\d+: (\S+):', std_out, re.MULTILINE)
ips = re.findall(r'inet (\d+\.\d+\.\d+\.\d+)/\d+', std_out)

if len(interfaces) < 2:
    print("Nu există a doua interfață")
else:
    second_interface = interfaces[1]
    print(f"A doua interfață: {second_interface}")

    # Căutăm IP-ul corespunzător a doua interfață
    pattern = re.compile(rf'{second_interface}.*?\n\s+inet (\d+\.\d+\.\d+\.\d+)/\d+', re.DOTALL)
    match = re.search(pattern, std_out)

    if match:
        print(f"{second_interface} are IP: {match.group(1)}")
    else:
        print(f"{second_interface} nu are IP. Setez unul...")
        ip_to_set = "192.168.1.100/24"
        # Setăm IP-ul și activăm interfața
        subprocess.Popen(['sudo', 'ip', 'addr', 'add', ip_to_set, 'dev', second_interface]).communicate()
        subprocess.Popen(['sudo', 'ip', 'link', 'set', second_interface, 'up']).communicate()
        print(f"IP-ul {ip_to_set} a fost setat pe {second_interface}")
