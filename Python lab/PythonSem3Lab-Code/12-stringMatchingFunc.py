'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	function to check if string matches specified string
title   :	experiment 12
'''

specified = 'india'

userInp = input("enter a string : ")

userInp = userInp.lower()

if userInp == specified:
    print("user entered 'india'")
else:
    print("specified string not detected in input")