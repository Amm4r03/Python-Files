import pandas as pd

data = {
    "calories" : [480, 380, 100],
    "duration" : [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

# read(df) ?