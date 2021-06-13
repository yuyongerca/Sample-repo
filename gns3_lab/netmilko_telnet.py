import netmiko

cisco_router ={
    "device_type": "cisco_ios_telnet",
    "host": "192.168.1.201",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco"
}
commands  = ['interface loopback0',
 'ip address 1.1.1.1 255.255.255.255',
 'end',
 'show run int loopback0']
netconnect = netmiko.ConnectHandler(**cisco_router)
netconnect.enable()
result = netconnect.send_command("show ip int brief",)
print (result)