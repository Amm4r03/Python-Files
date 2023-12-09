# prints range of fibonacci numbers to a certain number of terms 

numbers = int(input('enter the number of fibonacci numbers to be printed : '))

def fib(n):
    if(n > 1):
        return fib(n-2) + fib(n - 1)
    else:
        return 1

for i in range(numbers):
    print(fib(i))