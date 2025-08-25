import re
import subprocess

process = subprocess.Popen(["ip", "addr", "show"],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True)

stdout, stderr = process.communicate()

pattern = re.compile(r'inet(\d{1,3}\.\d+\.\d+\.\d+)/.global')
result = re.findall(pattern, stdout)

print(result)

result=re.search(pattern, stdout)
print(result.group(1))
