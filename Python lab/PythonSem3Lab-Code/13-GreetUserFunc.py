'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	function to greet user by taking name as input
title   :	experiment 13
'''

def greetUser(name):
    print("Hello {}, hope you are doing good".format(name))

n = input("enter your name : ")
greetUser(n)