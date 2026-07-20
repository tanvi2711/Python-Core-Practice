import pandas as pd

data = {
    'Name': ['Ramesh', 'Suresh', 'Jayesh', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    'Age': [50, 49, 23, 54, 56, 34, 37, 48],
    'Salary': [45000, 30000, 200000, 70000, 43000, 29000, 43000, 20000],
    'Performance_Score': [89, 50, 65, 76, 98, 87, 78, 90]
}

df = pd.DataFrame(data)

print(df)

# ==================================================
# Update a Specific Cell using .loc[]
# Syntax:
# df.loc[row_index, 'Column_Name'] = new_value
#
# .loc[] is used to access rows and columns by their labels.
# It is commonly used to update a single cell or multiple rows.
# ==================================================

# Update the Salary of the employee at row index 0
df.loc[0, 'Salary'] = 50000

print("\n\n", df)

# ==================================================
# Update an Entire Column
# Syntax:
# df['Column_Name'] = updated_values
#
# Here, each Salary value is increased by 5%.
# The operation is applied to every row (vectorized operation).
# ==================================================

df['Salary'] = df['Salary'] * 1.05

print('\n\n', df)