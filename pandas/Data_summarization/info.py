import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("DataSets/teachers.csv")

print("Dataset Info")

# info() displays a concise summary of the DataFrame:
# - Number of rows and columns
# - Column names
# - Number of non-null (non-missing) values
# - Data type of each column
# - Memory usage of the DataFrame
print(df.info())