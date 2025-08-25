import subprocess

result = subprocess.run(["ls"])
print(result)
result = subprocess.run(["ping", "-c", "4","8.8.8.8"])
print(result)
# result = subprocess.run(["python3.13" ""])
# print(result)

# Popen

process=subprocess.Popen(["echo", "test"],
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True,
                         text=True)

std_out, std_err=process.communicate()
print(type(std_out))
print(type(std_err))