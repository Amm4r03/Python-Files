# handling with errors returned in functions

def divByZero(number):
    try:
        return 42 / number
    except ZeroDivisionError:
        print('error : invalid arguemnt - division by zero')

print(divByZero(12))
print(divByZero(10))
print(divByZero(0))
print(divByZero(3))