'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	function to check for prime numbers in a given range (starting from 0 to n)
title   :	experiment 14
'''

def PrimeChecker(number):
    for num in range(1, number + 1):
        isPrime = True
        if num < 2:
            continue
        
        for divisors in range(2, int(num/2) + 1):
            if num % divisors == 0:
                isPrime = False
                break
        if isPrime:
            print(num, end=" ")
    
        
upper = int(input("enter the upper limit : "))

PrimeChecker(upper)