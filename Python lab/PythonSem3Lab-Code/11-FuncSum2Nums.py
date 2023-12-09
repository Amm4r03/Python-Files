'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	defines a function to sum 2 numbers
title   :	experiment 11
'''

def sum(a, b):
    return a+b

num1 = int(input("enter a number : "))
num2 = int(input("enter another number : "))

result = sum(num1, num2)
print("sum of both numbers is {}".format(result))