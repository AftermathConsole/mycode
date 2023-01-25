#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'This is what we think about your Internet speed: '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 25:
    message = message + 'That\'s more like it!'
elif connection >= 5:
    message = message + 'Barely worth it.'
elif connection >= 2:
    message = message + 'Time to upgrade.'
else:
    message = message + 'finding another access network.'
print(message)

