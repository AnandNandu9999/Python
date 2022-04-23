import pandas as pd

a = [1, 2, 3]

# printing the data in series
data = pd.Series(a)
print(data)

# modifying the index with our own index's
data = pd.Series(a, index=["a", "b", "c"])
print(data.loc(0))