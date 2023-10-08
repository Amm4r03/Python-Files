# code for reverse cipher

input = input('Enter a message : ')     # input from user
coded = ''                              # defined var to take in coded output

length = len(input) - 1                 # defined length of input (-1 to stay in string limit)

while length >= 0:
    coded = coded + input[length]       # increments string in 'coded' one character at a time
    length = length - 1                 # decrements value of length to add more characters until full string is traversed

print(coded)