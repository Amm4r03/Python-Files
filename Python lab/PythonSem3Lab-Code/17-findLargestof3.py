'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	code to determine largest of 3 numbers
title   :	experiment 17
'''

num1 = int(input("enter a number : "))
num2 = int(input("enter another number : "))
num3 = int(input("enter another number : "))

if num1 > num2:
    if num1 > num3 : 
        print("{} is the greatest of 3 input numbers".format(num1))
    else:
        print("{} is the greatest of 3 numbers".format(num3))
else:
    if num2 > num3:
        print("{} is the greatest of 3 numbers".format(num2))
    else: 
        print("{} is the greatest of 3 numbers".format(num3))