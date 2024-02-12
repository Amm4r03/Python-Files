# calc sum of digits of number (input by user)

number = int(input("enter your number : "))

sum = 0
for i in range(len(str(number))):
    digit = number % 10
    sum += digit
    number //=10

print("sum of digits of number : {}".format(sum))