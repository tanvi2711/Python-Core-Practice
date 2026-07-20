# ==================================================
# Summary Statistics
#
# Summary statistics are used to calculate important
# statistical information from a dataset, such as
# average, maximum, minimum, total, etc.
# ==================================================

import pandas as pd

data = {
    'Name': ['Varun', 'Arun', 'Jay'],
    "Age": [34, 65, 48],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)

print(df)

# ==================================================
# Calculate Mean (Average)
#
# Syntax:
# df['Column_Name'].mean()
#
# mean() returns the average value of all numeric
# values in the specified column.
#
# Formula:
# Mean = Sum of all values / Total number of values
# ==================================================

# Calculate the average salary of all employees
avg_salary = df['Salary'].mean()

print("Average Salary:", avg_salary)