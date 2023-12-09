# prints zigzag pattern

import time, sys

indent = 0
indentIncreasing = True

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.03) # Pause

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 30:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()