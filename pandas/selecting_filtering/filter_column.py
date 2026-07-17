import pandas as pd

# Sample employee dataset
data = {
    'Name': ['Ramesh', 'Suresh', 'Jayesh', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    'Age': [50, 49, 23, 54, 56, 34, 37, 48],
    'Salary': [45000, 30000, 200000, 70000, 43000, 29000, 43000, 20000],
    'Performance_Score': [89, 50, 65, 76, 98, 87, 78, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

print("Sample Data")
print(df)


# ============================================================
# Selecting a Single Column
# Returns a Pandas Series.
# Syntax: df["column_name"]
# ============================================================

print("\n\nName (Single Column - Returns a Series)")
name = df["Name"]
print(name)

# Another way (same output)
# print(df["Name"])


# ============================================================
# Selecting Multiple Columns
# Returns a Pandas DataFrame.
# Syntax: df[["column1", "column2"]]
# ============================================================

subset = df[["Name", "Salary"]]

print("\n\nSubset with Name and Salary")
print(subset)