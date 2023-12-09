# Ammar Ahmad Kidwai (2022-350-005)
# break statement
# input validation
# while True:
#     age = int(input("enter your age : "))
#     if age < 0:
#         print("please enter a valid age")
#     else:
#         break

# print("you are {} years old".format(age))

# auth. : Ammar Ahmad Kidwai (2022-350-005)
# topic : break statement
# title : linear search
list = [10, 20, 21, 26, 42, 56, 94]

key = int(input("enter the element to be searched : "))

for index,i in enumerate(list):
    if i == key:
        print("key found at {}".format(index))
        break
    elif i == list[-1]:
        print("key not found")