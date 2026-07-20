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

# df.fillna(0,inplace=True)
# print('\n\n', df)


# ==================================================
# Fill Missing Values
# Syntax:
# df['Column_Name'] = df['Column_Name'].fillna(value)
#
# fillna() replaces all missing (None/NaN) values
# in the specified column with the given value.
# ==================================================

# Fill missing values in the Age column with
# the mean (average) age of all employees.
df['Age'] = df['Age'].fillna(df['Age'].mean())

print('\n\n', df)

# Fill missing values in the Salary column with
# the mean (average) salary of all employees.
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print('\n\n', df)