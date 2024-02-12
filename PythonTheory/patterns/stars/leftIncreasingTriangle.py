height = int(input("enter the height of the triangle : "))

for i in range(1, height + 1):
    for j in range(i):
        print("*  ", end="")
    print()