#1/usr/bin/env python3
"""Understanding dictionaries
    {key: value, key:value,  ...} """

def main():
    """runtime function"""

    # Create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1.", "version": "1.2", "vendor": "Cisco"}

    # display the entire dictionary
    print(switch)

    # prove that it is indeed a dictionary
    print(type(switch))

    #display parts of the dictionary
    print( switch["hostname"] )
    print ( switch["ip"] )

    #request a "fake" key
    print( switch["lynx"] ) #this will cause the program to FAIL


    # call our main function
if __name__ == "__main_:_"
    main()
