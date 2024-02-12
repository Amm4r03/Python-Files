def factorial(num):
    if num == 2 or num == 1:
        return num
    else:
        return num * factorial(num - 1)

number = int(input("enter a number : "))

print(factorial(number))