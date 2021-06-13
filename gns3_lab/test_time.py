import netmiko
import datetime
#create lists for new router hostname and loopback ip
device_list =["gns3_lab_r1", "gns2_lab_r2", "gns3_lab_r3" ]
device_ip = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]
device_lan_ip = ["192.168.1.200", "192.168.1.201", "192.168.1.202"]
i = 0
#use netmiko connect to these three new routers
start_time = datetime.datetime.now()
while i < 3:
    

    cisco_router ={
        "device_type": "cisco_ios",
        "host": device_lan_ip[i],
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "port": 22
    }
    net_connect = netmiko.ConnectHandler(**cisco_router)
    net_connect.enable()
    result = net_connect.send_command('sh ip int brief')
    i = i+1
    net_connect.disconnect()
print (datetime.datetime.now() - start_time)
        