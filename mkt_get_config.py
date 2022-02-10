#!/bin/env python3

# pip3 install netmiko

import netmiko
from netmiko import ConnectHandler

mikrotik_router_1 = {
'device_type': 'mikrotik_routeros',
'host': '192.168.1.3',
'port': '22',
'username': 'admin',
'password': 'admin'
}

print("Handler is:%s" %mikrotik_router_1)

sshCli = ConnectHandler(**mikrotik_router_1)
output = sshCli.send_command("interface print")
print(output)

# print(sshCli.find_prompt())