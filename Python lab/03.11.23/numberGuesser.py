from random import randint

compNum = randint(0,10)

while True:
    userNum = int(input('Enter a number between 1-10 : '))
    if(userNum > 10 or userNum < 0):
        print('number out of bounds, try again')
    else:
        break

if (userNum > compNum):
    print('your number is larger than the number')
elif (userNum < compNum):
    print('your number is smaller than the number')
else:
    print('correct guess')        