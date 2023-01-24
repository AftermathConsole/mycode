#!/usr/bin/env python3
"""Alta3 Research |  DKEvans
   List - simple list """

def main():

    # create a list called list1
    list1 = ["cisoc_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display List1[1] which should only display arista_eos
    print(list1[1])

    # create a new list containing a single line
    list2 = ["Juniper"]

    # extend list1 by list2 (combine both lists together into a single list)
    list1.extend(list2)

    # display list1, which now contains juniper
    print(list1)

    # create list 3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #use the append operatin to append list1 by list3
    list1.append(list3)

    # display the new complex list1
    print(list1)

    # display the list of IP addresses
    print(list1[4])

    # display the first item in the list (0th item) - first IP address
    print(list1[4][0])

main()    
