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
# Remove Missing (Null) Data
#
# Syntax:
# df.dropna(axis=0, inplace=True)
#
# axis=0      -> Removes rows containing missing values.
# axis=1      -> Removes columns containing missing values.
# inplace=True -> Permanently updates the original DataFrame.
#
# Note:
# By default, dropna() removes rows if they contain
# at least one missing (None/NaN) value.
# ==================================================

df.dropna(axis=0, inplace=True)

print('\n\n', df)