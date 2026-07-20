import pandas as pd

data = {
    'EMP_ID': ['EMP_1', 'EMP_2', 'EMP_3', 'EMP_4', 'EMP_5', 'EMP_6', 'EMP_7', 'EMP_8'],
    'Name': ['Ramesh', 'Suresh', 'Jayesh', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    'Age': [50, 49, 23, 54, 56, 34, 37, 48],
    'Salary': [45000, 30000, 200000, 70000, 43000, 29000, 43000, 20000],
    'Performance_Score': [89, 50, 65, 76, 98, 87, 78, 90]
}

df = pd.DataFrame(data)

print(df)

# ==================================================
# Remove Column(s)
# Syntax:
# df.drop(columns=['Column_Name'], inplace=True)
#
# columns=[]  -> Specify one or more column names to remove.
# inplace=True -> Permanently removes the column from the DataFrame.
# ==================================================

# Remove a single column
df.drop(columns=['Performance_Score'], inplace=True)

print("\n\nTABLE AFTER DROPPING ONE COLUMN")
print(df)

# ==================================================
# Remove Multiple Columns
# Pass multiple column names inside the list.
# ==================================================

df.drop(columns=['Age', 'EMP_ID'], inplace=True)

print("\n\nTABLE AFTER DROPPING MULTIPLE COLUMNS")
print(df)