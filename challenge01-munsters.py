#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
         'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------

# display the value mapped to names
print(munsters.get("names"))

# display the value mapped to endDate.
print(munsters.get("endate"))

# display the value mapped to startDate
print(munsters.get("startDate"))

# add new key, episodes mapped to the value of 70.
munsters.append{"episodes": 70}

