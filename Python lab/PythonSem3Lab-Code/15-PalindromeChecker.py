'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	check if a string is a palindrome or not
title   :	experiment 15
'''

inpStr = input("enter a string : ")

inpStr = inpStr.lower().replace(" ", "")

revStr = inpStr[::-1]       # reverse string by slicing (negative step value)

if inpStr == revStr:
    print("input word is a palindrome")
else:
    print("input string is not a palindrome")