import pandas as pd

data = {
    'Name': ['Varun', 'Arun', 'Jay', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    "Age": [34, 23, 48, 23, 54, 56, 23, 34],
    "Salary": [50000, 45000, 30000, 200000, 70000, 43000, 29000, 43000]
}

df = pd.DataFrame(data)

print(df)

# ==================================================
# GroupBy using Multiple Columns
#
# Syntax:
# df.groupby(['Column1', 'Column2'])['Target_Column'].sum()
#
# Parameters:
# ['Age', 'Name'] -> Groups the data using both Age
#                    and Name columns.
# ['Salary']      -> Selects the Salary column for
#                    aggregation.
# sum()           -> Calculates the total Salary for
#                    each Age-Name combination.
#
# Note:
# Data is first grouped by Age and then by Name.
# Each unique combination forms a separate group.
# ==================================================

# Group employees by both Age and Name, then calculate
# the total Salary for each group.
groupby = df.groupby(['Age', 'Name'])['Salary'].sum()

print(groupby)