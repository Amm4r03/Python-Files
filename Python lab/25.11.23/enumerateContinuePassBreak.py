# ammar ahmad kidwai (2022-350-005)

# continue, break, pass, enumerate


# enumerate()
# iterate through list of days
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for i, day in enumerate(days, start=1):
    print(i, day)

# numbers = [10, 20, 30, 40, 50]
# element_sum = 0
# 
# for i, val in enumerate(numbers):
#     element_sum = element_sum + val
#     print(i, element_sum)

# break

# input validation
# while True:
#     age = int(input("enter your age : "))
#     if age < 0:
#         print("please enter a valid age")
#     else:
#         break

# print("you are {} years old".format(age))

# # linear search
# list = [10, 20, 21, 26, 42, 56, 94]

# key = int(input("enter the element to be searched : "))

# for index,i in enumerate(list):
#     if i == key:
#         print("key found at {}".format(index))
#         break
#     elif i == list[-1]:
#         print("key not found")

# pass

# # prints odd numbers in a range
# lower = int(input("enter the lower limit : "))
# upper = int(input("enter the upper limit : "))

# for i in range(lower, upper):
#     if i%2==0:
#         pass
#     else:
#         print(i)
      

# continue statement
# # removes vowels from string
# 
# sen = input("enter a string : ")
# 
# lowerSen = sen.lower()
# 
# print("input string without vowels : ", end="")
# for i in lowerSen:
#     if i in 'aeiou':
#         continue
#     else:
#         print("{}".format(i), end="")
