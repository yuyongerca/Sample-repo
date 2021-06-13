import netmiko

cisco_router ={
    "device_type": "cisco_ios",
    "host": "192.168.1.202",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
    "port": 22
}
commands  = ['interface loopback0',
 'ip address 1.1.1.1 255.255.255.255',
 'end',
 'show run int loopback0']
netconnect = netmiko.ConnectHandler(**cisco_router)
netconnect.enable()
result = netconnect.send_command("show ip int brief",)
print (result)
result =  netconnect.send_config_set(commands)
print (result)
result = netconnect.send_config_from_file('lab_r1.txt')
print (result)