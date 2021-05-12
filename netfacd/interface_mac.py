#!/usr/bin/env python3

import netifaces
print('\n**************Details of Interface - ' + i + ' *********************')
adapter = input("choose an adapter:")
return_mac(adapter)

def return_mac(adapter):
    for i in netifaces.interfaces():
        if adapter == i:
          print('MAC: ', end='')  # This print statement will always print MAC without an end of line
          print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
