height = int(input("enter the height of the triangle : "))

for line in range(1, height + 1):
    for char in range(1, line + 1):
        print(char, end="  ")
    print()