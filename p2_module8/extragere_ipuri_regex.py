import re
text = """
Server1: 192.168.1.10
Server2: 10.0.0.5
Loopback: 127.0.0.1
"""

pattern = re.compile(r'(?<!127\.)\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b') #exclude loopback
ips = pattern.findall(text)
print(ips)
