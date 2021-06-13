import paramiko
import time
import os
import sys
netconnect = paramiko.SSHClient()
netconnect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
netconnect.connect('192.168.1.200',22, username='cisco', password='cisco')
print ("running remote command")


##read the config file and implement config lines in this file
with open('lab_sw1.txt', 'r', encoding='utf-8') as infile:
    connection = netconnect.invoke_shell()
    connection.send('enable\n')
    time.sleep(1)
    connection.send('cisco\n')
    connection.send('term len 0\n')
    for line in infile:
        connection.send(line+'\n')
        time.sleep(1)
        file_output_file = connection.recv(99999).decode(encoding='utf-8')
        print(file_output_file)




