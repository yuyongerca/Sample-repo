import netmiko
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

ip_add_list = ['192.168.1.200', '192.168.1.201', '192.168.1.202']


def ssh_connec (list,command,filename):
    cisco_device ={
    "device_type": "cisco_ios",
    "host": list,
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    "port": 22
    }
    net_conn = netmiko.ConnectHandler(**cisco_device)
    net_conn.enable()
    result = net_conn.send_command(command)
    print (result)
    with open(filename, 'a') as outfile:
        outfile.write(result +'\n')
with ThreadPoolExecutor(max_workers=3) as excutor:
    future_result ={excutor.submit(ssh_connec, list, 'sh ip int brief',list +'.txt'): list for list in ip_add_list} 
    for f in as_completed(future_result):
        print (future_result[f],"job done")
