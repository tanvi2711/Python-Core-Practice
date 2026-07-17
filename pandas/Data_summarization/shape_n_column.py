import pandas as pd

data = {
    'Name': ['Ramesh', 'Suresh', 'Jayesh', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    'Age': [50, 49, 23, 54, 56, 34, 37, 48],
    'Salary': [45000, 30000, 200000, 70000, 43000, 29000, 43000, 20000],
    'Performance_Score': [89, 50, 65, 76, 98, 87, 78, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

print(df)

# shape returns a tuple (rows, columns)
# Helps determine the size of the dataset.
print("Shape: ", df.shape)

# columns returns the names of all columns
# Useful for understanding the dataset structure.
print("Columns: ", df.columns)

