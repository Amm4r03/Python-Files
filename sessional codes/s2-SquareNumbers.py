def squareNums():
    for i in range(1, 8):
        yield i**2

for square in squareNums():
    print(square)