# numbers

a = 20
b = 10

sum = a + b
sub = a - b

print('{} is the sum of {} and {}'.format (sum, a, b)) # using curly braces as placeholders

print('{2} is the subtraction of {0} and {1}'.format (a, b, sub))   # mentioning index of paramter to be printed 
# paramters in .format are zero indexed

print("the sum of %d and %d is %d" %(a, b, sum)) # using % format specifier 