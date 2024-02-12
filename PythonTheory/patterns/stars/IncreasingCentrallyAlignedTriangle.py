'''
   *
  ***
 *****
'''

height = int(input("enter the height of the triangle : "))

for line in range(height):
    # print spaces
    for space in range(height - line):
        print(" ", end = "")
    
    # print stars
    for stars in range(height - space):
        print("* ", end="")
    
    # print newline
    print()