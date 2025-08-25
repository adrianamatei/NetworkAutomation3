import subprocess
name=input('give name: ')
print(f'hello, {name}')
process=subprocess.Popen(["python.exe", r'C:\Users\Ionela\PycharmProjects\NetworkAutomation3\p2_module8\comunicate_with.py'],
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True,
                         text=True)
std_out, std_err=process.communicate('test')
print(std_out)
print(std_err)