'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	prints fibonacci in range
title   :	experiment 20
'''

upper = int(input("enter the number of terms to be printed : "))

def printFibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return printFibonacci(num - 1) + printFibonacci(num - 2)

for i in range(0, upper):
    print(printFibonacci(i), end=" ")