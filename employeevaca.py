#!/usr/bin/env python3

print("How many years have you been and employee: ")
emyears = int(input())
if emyears >= 30:
    vacadays = emyears * 3
elif emyears >= 20:
    vacadays = emyears * 2
elif emyears >= 10:
    vacadays = emyears * 1.5
else:
    vacadays = emyears * 1
print("You have ", vacadays, " vacation days.")
