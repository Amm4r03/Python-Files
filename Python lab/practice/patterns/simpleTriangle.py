'''
*
*     *
*     *       *
'''
rows = int(input('enter the number of rows of pattern to be printed : '))
rows += 1

for i in range(rows):
    for j in range(i):
        print("*", end="  ")    # prints the star with the space at the end (to ensure output doesnt move to next line)
    print("")                   # prints the newline character (at the end of each line)