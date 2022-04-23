import pandas as pd

DataFrame = pd.read_csv("data")

data = DataFrame.to_string()

# type is str
print(type(data))

# it prints the data
print(data)

print(DataFrame.loc[0])


