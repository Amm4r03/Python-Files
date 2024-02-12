height = int(input("enter height of triangle : "))

for i in range(height):
    for j in range(height - i):
        print('* ', end = "")
    print()