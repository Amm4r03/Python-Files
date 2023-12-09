# auth. : Ammar Ahmad Kidwai (2022-350-005)
# topic : continue statement
# title : remove vowels from string

sen = input("enter a string : ")

lowerSen = sen.lower()

print("input string without vowels : ", end="")
for i in lowerSen:
    if i in 'aeiou':
        continue
    else:
        print("{}".format(i), end="")