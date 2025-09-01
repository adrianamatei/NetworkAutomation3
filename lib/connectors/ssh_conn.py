import time

import paramiko

HOST = '192.168.200.10' #adresa  IOU1
PORT = 5120  # replace with yours

class SshConnection:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssh=None

    def __enter__(self):
        return self

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
        )

    def write(self, data: str):
        pass


    async def configure(self):
       stdin,stdout,stderr=self.ssh.exec_command('show version')
       time.sleep(1)
       print(stdout.read())

    async def close(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.write('\n')

if __name__ == '__main__':
    conn = SshConnection(HOST, PORT,'ionela','ionela123')
    conn.connect()
    conn.configure()



