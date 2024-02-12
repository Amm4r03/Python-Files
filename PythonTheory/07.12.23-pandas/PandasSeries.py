# pandas series

import pandas as pd

a = [1, 2, 7]

myVar = pd.Series(a, index=['x', 'y', 'z'])

print(myVar)