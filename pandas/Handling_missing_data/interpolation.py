# ==================================================
# Interpolation
#
# Interpolation estimates missing (None/NaN) values
# using nearby available values instead of removing
# the data.
#
# Benefits:
# - Preserves data integrity.
# - Maintains smooth data trends.
# - Avoids unnecessary data loss.
# ==================================================

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
# Interpolate Missing Values
# Syntax:
# df['Column_Name'] = df['Column_Name'].interpolate(method='linear')
#
# method='linear' estimates missing values using
# the nearest previous and next numeric values.
# ==================================================

df['Age'] = df['Age'].interpolate(method='linear')
df['Salary'] = df['Salary'].interpolate(method='linear')
df['Performance_Score'] = df['Performance_Score'].interpolate(method='linear')

print("\n\n", df)


# ==================================================
# How Linear Interpolation Works
#
# Formula:
# Estimated Value = (Previous Value + Next Value) / 2
#
# Since Dhiraj's row contains missing values:
#
# Age:
# (23 + 56) / 2 = 39.5
#
# Salary:
# (200000 + 43000) / 2 = 121500.0
#
# Performance Score:
# (65 + 98) / 2 = 81.5
#
# After interpolation, Dhiraj's row becomes:
#
# EMP_ID   Name     Age   Salary    Performance_Score
# EMP_4    Dhiraj   39.5  121500.0  81.5
# ==================================================