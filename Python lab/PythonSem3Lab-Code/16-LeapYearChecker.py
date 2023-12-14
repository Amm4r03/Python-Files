'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	checks for leap year
title   :	experiment 16
'''

year = int(input("enter the year : "))

if year % 100 == 0:
    if year % 400 == 0:
        print("leap year")
    else:
        print("not a leap year")
else:
    if year % 4 == 0:
        print("leap year")
    else:
        print("not a leap year")
