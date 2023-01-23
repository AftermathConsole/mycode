#!/usr/bin/env python3
"""Alta3 Research | DKEvans
   print() - concatenate vs print a series of items"""

def main():

    #collect string input from the user
    user_input = input("Please enter an IPv4 IP address: ")

    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input

    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is : ", user_input)

    ##obtain the vendor name for that IP address
    user_input2 = input2("Please tell me the vendor associated with this IP: ")
    
    ##give the vendor name back to verify it.
    print("You told me the vendor name is: ", user_input2)


main()
