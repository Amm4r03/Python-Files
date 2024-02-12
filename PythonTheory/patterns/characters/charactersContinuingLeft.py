height = int(input("enter the height of the pattern : "))

start = 65

for line in range(1, height + 1):
    for char in range(line):
        print(chr(start), end=" ")
        start += 1
    print()