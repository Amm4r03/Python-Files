# prints the prime numbers within a range (input by user)

lower = int(input('enter the lower bound value : '))
upper = int(input('enter the upper bound value : '))

for i in range (lower, upper+1):
    flag = True
    for x in range(2, int(upper/2)):
        if (i % x == 0):
            flag = False
            break
    if flag:
        print(i)