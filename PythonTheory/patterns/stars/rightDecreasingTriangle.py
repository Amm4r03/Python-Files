'''
***
 **
  *
'''

height = int(input('enter the height of the triangle : '))

# starts from 1 to avoid blank line; runs till height + 1 to ensure `height` lines in output
for line in range(1, height + 1):
    
    # print spaces
    for spaces in range(height - line):
        print("   ", end="")
    
    # print stars
    for stars in range(line):
        print("*  ", end="")

    # add newline characters
    print()