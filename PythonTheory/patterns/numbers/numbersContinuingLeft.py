height = int(input('enter the height of the pattern : '))

start = 1
for line in range(1,height + 1):
    for char in range(line):
        print(start, end="\t")
        start += 1
    print()