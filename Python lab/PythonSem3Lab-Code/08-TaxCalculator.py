'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	Tax calculator
title   :	experiment 8
'''

cost = int(input("Enter the price of the bike : "))

if cost > 150000:
    taxBrack = 15
    tax = cost * 0.15
elif cost > 50000 and cost < 150000:
    tax = cost * 0.1
    taxBrack = 10
else:
    tax = 0
    taxBrack = 0

totalCost = tax + cost

print("Tax Calculator\nVehicle Price : {}\nTax% : {}%\nTax applicable : {} INR\nTotal payable : {} INR".format(cost, taxBrack, tax, totalCost))

# test input : 11858