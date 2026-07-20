import pandas as pd

data = {
    'Name': ['Varun', 'Arun', 'Jay'],
    "Age": [34, 65, 48],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)

print(df)

# ==================================================
# Sort by Multiple Columns
#
# Syntax:
# df.sort_values(by=['Column1', 'Column2'],
#                ascending=[True/False, True/False],
#                inplace=True)
#
# Parameters:
# by         -> List of columns used for sorting.
# ascending  -> Specify sorting order for each column.
#               True  = Ascending Order
#               False = Descending Order
# inplace    -> Permanently updates the DataFrame.
#
# Note:
# The DataFrame is first sorted by the first column.
# If duplicate values exist, the second column is
# used to break the tie.
# ==================================================

# Sort by Age in Ascending Order.
# If two employees have the same Age, they will be
# sorted by Salary in Descending Order.
df.sort_values(by=['Age', 'Salary'], ascending=[True, False], inplace=True)

print("Sorted by Age (Ascending) and Salary (Descending)")

print("\n\n", df)