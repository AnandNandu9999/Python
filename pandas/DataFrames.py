import pandas as pd

data = {
    "days": ["Monday", "Tuesday", "Wednesday"],
    "series": [1, 2, 3]
}

# load data into a DataFrame object
dataframe = pd.DataFrame(data)
print(dataframe)

# Locate Row
print(dataframe.loc[[0, 1]])