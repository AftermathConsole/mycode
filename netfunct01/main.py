#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'Handshakinig, .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll lear to write code that sends cmds to device here
    return None

    # start our main script
def main():
        """called at runtime"""

        # dict containing IPs mapped to a list of physical interfaces and their state.
        devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

        print("Welcome to the network device command pusher") # welcome message.

        # Get data set
        print("\nData set found\n") # replace with function call that reads in data from file

        # run
        commandpush(devicecmd) # call function to push commands to devices


# call our main function
main()

