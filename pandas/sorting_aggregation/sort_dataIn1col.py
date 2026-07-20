# ==================================================
# Sorting Data
#
# Sorting arranges data in ascending or descending
# order based on one or more columns.
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
# Sort by a Single Column
#
# Syntax:
# df.sort_values(by='Column_Name',
#                ascending=True/False,
#                inplace=True)
#
# Parameters:
# by         -> Column used for sorting.
# ascending  -> True  = Ascending order (Default)
#               False = Descending order
# inplace    -> Permanently updates the DataFrame.
# ==================================================

# Sort the DataFrame by Age in Descending Order
df.sort_values(by='Age', ascending=False, inplace=True)

print("Sorted Age in Descending Order")

print("\n\n", df)

# Sort the DataFrame by Age in Ascending Order
df.sort_values(by='Age', ascending=True, inplace=True)

print("Sorted Age in Ascending Order")

print("\n\n", df)


