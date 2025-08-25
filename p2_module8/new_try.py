import subprocess
import os
result= subprocess.run(["ls"])
print(result)

#Popen
process=subprocess.Popen(['echo','test'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
#out=process.communicate()
#print(type(out))
std_out,std_err=process.communicate()
print(type(std_out))
print(type(std_err))