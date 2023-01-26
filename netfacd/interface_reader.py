#!/usr/bin/env python3

import netifaces
# bring in the module we'll need for this lab.

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # prints the MAC address
        # uses the module netifaces, tool ifaddresses of (interfacename) then uses the tool AF_LINK, then chooses the device at
        # index [0], and types addr
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # prints the IP address
    except: # this is a new line
        print('Could not collect adapter information') # print an error message.
