# # Ammar Ahmad Kidwai (2022-350-005)
# # enumerate()
# # iterate through list of days
# days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# for i, day in enumerate(days, start=1):
#     print(i, day)

# Ammar Ahmad Kidwai (2022-350-005)
# sum of elements in list
numbers = [10, 20, 30, 40, 50]
element_sum = 0

for i, val in enumerate(numbers):
    element_sum = element_sum + val
    print(i, element_sum)
