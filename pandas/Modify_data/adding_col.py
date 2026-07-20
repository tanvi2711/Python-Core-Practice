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
# Add a New Column
# Syntax:
# df['Column_Name'] = values
#
# If the column already exists, its values are updated.
# If it doesn't exist, Pandas creates a new column.
# ==================================================

# Add a Bonus column containing 10% of each employee's salary
df['Bonus'] = df['Salary'] * 0.1

print('\n\n', df)

# ==================================================
# Insert a Column at a Specific Position
# Syntax:
# df.insert(location, 'Column_Name', values)
#
# location = Column index where the new column should appear
# 0 means insert at the beginning (first column)
#
# Note:
# insert() gives an error if the column name already exists.
# ==================================================

df.insert(
    0,
    'EMP_ID',
    ['EMP_1', 'EMP_2', 'EMP_3', 'EMP_4', 'EMP_5', 'EMP_6', 'EMP_7', 'EMP_8']
)

print("\n\n", df)