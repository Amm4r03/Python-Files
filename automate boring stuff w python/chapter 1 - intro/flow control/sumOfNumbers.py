# makes use of for loop to calculate sum of numbers going from 0 to a number input by user

total = 0

number = int(input('Enter a number : '))

for i in range (number+1):
    total = total + i

print(total)