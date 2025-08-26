import subprocess
import time

process=subprocess.Popen(
    ['ping','8.8.8.8'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
start_time=time.time()
count=0
while True:
    line=process.stdout.readline()
    if line ==' ' and process.poll() is not None: #poll->None inseamna ca procesul inca ruleaza, altceva inseamna ca procesul s-a terminat
        break
    if line:
        print(line.strip())
        if 'bytes from' in line:
            count=count+1
    if time.time()-start_time>5:
        process.terminate() #opreste procesul care ruleaza
        break
print(f"Pachete primite: {count}")