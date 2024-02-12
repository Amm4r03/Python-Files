'''
   *
  **
 ***
****
'''

height = int(input("enter the height of the triangle : "))

for line in range(1, height + 1):
    # print spaces
    for spaces in range(height - line):
        print("   ", end="")
    
    # print stars
    for stars in range(line):
        print("*  ", end="")
    
    print()