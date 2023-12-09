# auth. : Ammar Ahmad Kidwai (2022-350-005)
# topic : pass statement
# title : print odd numbers in a range
lower = int(input("enter the lower limit : "))
upper = int(input("enter the upper limit : "))

for i in range(lower, upper):
    if i%2==0:
        pass
    else:
        print(i)