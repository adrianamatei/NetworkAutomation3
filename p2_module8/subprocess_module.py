''''#2 metode de a executa un proces, metoda run si cea cu obiect
import subprocess

result= subprocess.run(["dir"],shell=True)
print(result)
result= subprocess.run(["ping",'8.8.8.8'])
print(result)'''

'''
import sys
print(sys.path)
import subprocess
result=subprocess.run(["ls"])
print(result)'''
import subprocess
import os
result= subprocess.run(["ping",'8.8.8.8'])
print(result)
'''result= subprocess.run(["notepad"])
print(result)
result=subprocess.run(["python3.11" 'C:\\Users\Ionela\PycharmProjects\\NetworkAutomation3\p2_module7\ex2.py'])
print(result)'''
