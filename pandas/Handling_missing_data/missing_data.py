import pandas as pd

data = {
    'EMP_ID': ['EMP_1', 'EMP_2', 'EMP_3', 'EMP_4', 'EMP_5', 'EMP_6', 'EMP_7', 'EMP_8'],
    'Name': ['Ramesh', 'Suresh', 'Jayesh', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    'Age': [50, 49, 23, None, 56, 34, 37, 48],
    'Salary': [45000, 30000, 200000, None, 43000, 29000, 43000, 20000],
    'Performance_Score': [89, 50, 65, None, 98, 87, 78, 90]
}

df = pd.DataFrame(data)

print(df)

# ==================================================
# Detect Missing Values
#
# In Pandas, missing values such as None or NaN are
# treated as missing data.
#
# Method:
# df.isnull()
#
# Returns:
# True  -> Missing value found
# False -> Value is present
# ==================================================

print('\n\n', df.isnull())

# ==================================================
# Count Missing Values
#
# Syntax:
# df.isnull().sum()
#
# .isnull() identifies missing values.
# .sum() counts the number of True values in each column.
# ==================================================

print("\n\n", df.isnull().sum())