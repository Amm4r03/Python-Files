'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	prints even numbers in given range
title   :	experiment 18
'''

lower = 0
upper = 50

for i in range(lower, upper):
    if i % 2 == 0:
        print(i, end = " ")
