import pandas as pd

# printing the pandas version
print(pd.__version__)

# fetching data from CSV file
DataFrame = pd.read_csv("data")

print(DataFrame.to_string())

# Creating the DataFrame in python code
my_data_frame = {
    "country": ["India", "Australia", "Canada", "America"],
    "code": [91, 92, 93, 94]
}

print("+" * 100)
print(my_data_frame)
print("+" * 100)

print(pd.DataFrame(my_data_frame))

