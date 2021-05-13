from netmiko import ConnectHandler
from getpass import getpass

arista = {
    "device_type": "arista_eos",
    "host": "sw-1",
    "username": "admin",
    "password": getpass(),
}

# Show command that we execute.
command = "show ip int brief"

with ConnectHandler(**arista) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()
