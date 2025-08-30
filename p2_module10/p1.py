# add multiple routes in parllel using multi processing

import multiprocessing as mp
import os
import time
import subprocess



def add_routes(dest_ip, next_hop):
    subprocess.run(['ip', 'route', 'add', f'{dest_ip}/24', 'via', f'{next_hop}'])
    #eu nu am nevoie de asta ca am deja adresa ip


if __name__ == '__main__':
    #subprocess.run(['ip', 'addr', 'add', '192.168.100.100/24', 'dev', 'ens4'])
    processes=[]
    for i in range(1,5):
        p=mp.Process(target=add_routes,args=(f'192.168.10{i}.0',f'192.168.10{i}.1',))
        processes.append(p)
    print("Starting to set routes")
    for proc in processes:
        proc.start()
    print("Setting routes")
    for proc in processes:
        proc.join()

    print("Both processes finished")