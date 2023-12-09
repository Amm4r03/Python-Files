# prints n terms of the fibonacci sequence

terms = int(input('enter the terms of fibonacci sequence to be printed : '))

def fib(n):
    if(n > 0):
        return fib(n-2) + fib(n - 1)
    else:
        return 1

print(fib(terms))