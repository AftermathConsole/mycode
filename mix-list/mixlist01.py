#!/usr/bin/env python3

# create a list of three items
my_list = ( "192.168.0.5", 5060, "UP")


# create a list of six items
iplist = [ 5060, "80",  55, "10.0.0.1", "10.20.30.1", "ssh" ] 

# using our '+' 
print( "IP address: " + iplist[3] + ", and " + iplist[4])

# use the comma separator
print("IP Address: " + iplist[3] + ", and " + iplist[4])

# use the f-string
print(f"IP Address: {iplist[3]}, and {iplist[4]}")

# display the first item
print("The first item in the list (IP): " + my_list[0])

# display the second item
print("The sedond item in the list (port): " +str(my_list[1]))


# display the last item in the list
print("The last item in the list (state): " + my_list[2])
