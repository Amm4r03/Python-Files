'''
    *
   ***
  *****
   ***
    *
'''

height = int(input("Enter the height of the diamond: "))

# Upper half of the diamond
for i in range(1, height + 1, 2):
    spaces = (height - i) // 2
    stars = i
    print(" " * spaces + "*" * stars)

# Lower half of the diamond
for i in range(height - 2, 0, -2):
    spaces = (height - i) // 2
    stars = i
    print(" " * spaces + "*" * stars)