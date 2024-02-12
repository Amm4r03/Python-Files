printUpper = input('Print for\nlowercase: 1\nuppercase: 0\nEnter your choice: ')

start = 97 if printUpper == '1' else 65

height = int(input('enter the height of the pattern : '))

for line in range(1, height + 1):
    for char in range(line):
        print(chr(start + char), end=" ")
    print()