# # Ammar Ahmad Kidwai (2022-350-005)
# # check for even numbers in a given range
# lower = int(input("enter the lower limit for range : "))
# upper = int(input("enter the upper limit for range : "))

# print("even numbers between {} and {} are : ".format(lower, upper))
# for i in range(lower, upper):
#     if i%2 == 0:
#         print(i, end=" ")


# # Ammar Ahmad Kidwai (2022-350-005)
# # sum of 0 to n numbers
# num = int(input("enter a number : "))
# sum = 0 

# for i in range(0, num+1):
#     sum = sum + i
# print("sum = {}".format(sum))

# Ammar Ahmad Kidwai (2022-350-005)
# factorial calculator
num = int(input("Enter a number : "))
print("{}! ".format(num), end="")

prod = 1
while num > 0:
    prod = prod * num
    num = num - 1

print("= {}".format(prod))