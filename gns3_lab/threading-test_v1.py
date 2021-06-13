# import logging
# import threading
# import time
# import concurrent.futures

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(thread_function, range(3))

from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
import logging

import yaml
import netmiko
start_time = datetime.now()

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show(device, show):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received:   {}'
    ip = device['ip']
    logging.info(start_msg.format(datetime.now().time(), ip))
    if ip == '192.168.100.1':
        time.sleep(5)

    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show)
        logging.info(received_msg.format(datetime.now().time(), ip))
        return result
def send_command_to_devices(devices, command):
    data = {}
    with ThreadPoolExecutor(max_workers=2) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            
            data[device['ip']] = output
            
    return data


if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        print (type(devices))
    pprint(send_command_to_devices(devices, 'sh ip int br'))
print (datetime.now() - start_time)

# with open('devices.yaml') as f:
#     devices = yaml.safe_load(f)

# with ThreadPoolExecutor(max_workers=3) as executor:
#     result = executor.map(send_show, devices, repeat('sh clock'))
#     for device, output in zip(devices, result):
#         print(device['ip'], output)