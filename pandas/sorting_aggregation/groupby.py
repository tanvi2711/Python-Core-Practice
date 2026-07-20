# ==================================================
# GroupBy and Aggregation
#
# GroupBy is used to divide the data into groups
# based on one or more columns. Aggregation
# functions are then applied to each group to
# calculate summary values.
# ==================================================

import pandas as pd

data = {
    'Name': ['Varun', 'Arun', 'Jay', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    "Age": [34, 23, 48, 23, 54, 56, 23, 34],
    "Salary": [50000, 45000, 30000, 200000, 70000, 43000, 29000, 43000]
}

df = pd.DataFrame(data)

print(df)

# ==================================================
# Group Data and Apply Aggregation
#
# Syntax:
# df.groupby('Column_Name')['Target_Column'].sum()
#
# groupby()       -> Groups rows having the same value.
# ['Salary']      -> Selects the column for calculation.
# sum()           -> Calculates the total salary for
#                    each Age group.
# ==================================================

# Group employees by Age and calculate the total Salary
# for each age group.
groupby = df.groupby('Age')['Salary'].sum()

print(groupby)

