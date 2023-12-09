# takes input from user for name and age and saves in a file

name = input('please enter your name : ')
age = input('please enter your age : ')

with open("nameAndAge.txt", "w+") as sampleFile:
    sampleFile.write(name + ' ' + age)
    sampleFile.seek(0)
    savedContent = sampleFile.read()

print('{}\n\ninformation saved successfully in file'.format(savedContent))