input_string = input('enter the string : ')

input_string = input_string.replace(" ", "")        # removes all whitespaces using replace()
input_string = input_string.lower()                 # turns string to lowercase for comparison

reverse_string = input_string[::-1]

if (input_string == reverse_string):
    print('input is a palindrome')
else:
    print('input is not a palindrome')