'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	electricity bill calculator on given rubric
title   :	experiment 7
'''

units = int(input("Enter the number of units consumed : "))

if units <= 50:
    bill = 100
elif units > 50 and units <300:
    bill = units * 4.5
else:
    payableUnits = units - 300
    bill = 1000 + payableUnits * 7

print("ELECTRICITY BILL\nUnits Consumed : {} kWh\nAmount Payable : {} INR".format(units, bill))