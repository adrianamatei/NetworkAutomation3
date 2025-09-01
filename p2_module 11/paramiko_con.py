import threading
import time
from lib.connectors.ssh_conn import SshConnection
#sa configuram cele doua device uri si sa dam ping din ssh
HOST='192.168.200.10'
PORT=22
USER='ionela'
PASS='ionela123'

devices=[
    {
        "host":"192.168.200.10",
        "port":22,
        "username":'ionela',
        "password":'ionela123',
    },
    {
        "host":"192.168.200.3",
        "port":22,
        "username":'ionela',
        "password":'ionela123',
    }
]
def configure_ip(host,port,username,password):
    ssh=SshConnection(host=host,port=port,username=username,password=password)
    ssh.connect()
    ssh.configure()
threads=[]
for device in devices:
    t=threading.Thread(target=configure_ip,args=(device['host'],device['port'],device['username'],device['password']))
    threads.append(t)
for thd in threads:
    thd.start()
