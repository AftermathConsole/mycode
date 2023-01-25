#!/usr/bin/env python3
"""For - looping across a file opened with 'with'
        while also being gentle on memory consumption."""

# open a file in read mode.
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:  # we never created a list of lines to store in memory
        # print and end without a new line
        print(svr, end="")

# no need to close our file - closed automatically.
