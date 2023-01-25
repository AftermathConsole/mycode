#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

# ask the user for their grade in points that they received.
gradescore = int(input("If you tell me what What point grade you got on the test, I will tell you what old-school grade you would have gotten. \nHow many points on the test did you get? "))

# message that tells you what you would have received
message = "Then you would have received a"

# if input value was higher than zero or equal to 100
if gradescore >= 90:
    message = + 'n A. Great job!'
elif gradescore >= 80:
    message = message + ' B. Pretty good.'
elif gradescore >= 70:
    message = message + ' C. Considered Average, but you could improve.'
elif gradescore >= 60:
    message = message + ' D. Very low, get to sleep earlier and do some studying.'
elif gradescore <= 59:
    message = message + ' F. A failing grade. Welcome to manual labor'
else:
    print("Please type in a number from 0 to 100")
print(message)

