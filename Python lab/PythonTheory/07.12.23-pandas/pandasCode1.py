# testing python

import pandas

myDataset = {
            'cars' : ["BMW", "volvo", "ford"],
            'passings' : [3,7,2]
            }

myVar = pandas.DataFrame(myDataset)

print(myVar)