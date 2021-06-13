import netmiko

#create lists for new router hostname and loopback ip
device_list =["gns3_lab_r1", "gns2_lab_r2", "gns3_lab_r3" ]
device_ip = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]
device_lan_ip = ["192.168.1.200", "192.168.1.201", "192.168.1.202"]
i = 0
#use netmiko connect to these three new routers

while i < 3:
    
    with open("lab_template_config.txt", "rt") as template:
        with open(device_list[i] + ".txt", "wt") as new_file:
            for line in template:
                if "host_tem"  in line:
                    line = line.replace("host_tem",device_list[i], -1)
                elif "x.x.x.x"  in line:
                    line = line.replace("x.x.x.x",device_ip[i], -1)
                new_file.write(line)
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
    result = net_connect.send_config_from_file(device_list[i] + ".txt")
    i = i+1
    net_connect.disconnect()
        