#!/usr/bin/env python3

import netifaces
import argparse

print(netifaces.interfaces())

def parze(options):
    parser = argparse.ArgumentParser(description='data related to network interfaces.')
    parser.add_argument('interface_name', help='name of the interface.')
    return parser.parse_args()
for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
output = parze("lo")
print(output)
name_test = output[args.interface_name]
print(ip_test(args.ip_address))
    
