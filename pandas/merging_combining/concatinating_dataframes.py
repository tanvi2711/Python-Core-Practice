# ==================================================
# Concatenating DataFrames
#
# Syntax:
# pd.concat([df1, df2],
#           axis=0,
#           ignore_index=True)
#
# concat() combines two or more DataFrames either
# vertically (rows) or horizontally (columns).
# ==================================================

import pandas as pd

df_region1 = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Ramesh", "Suresh", "Dinesh"]
})

df_region2 = pd.DataFrame({
    "CustomerID": [4, 5, 6],
    "Name": ["Mangesh", "Chaman", "Diya"]
})

# ==================================================
# Vertical Concatenation
#
# Syntax:
# pd.concat([df1, df2],
#           axis=0,
#           ignore_index=True)
#
# Parameters:
# axis=0            -> Combines DataFrames row-wise
#                      (Default).
# ignore_index=True -> Creates a new sequential index
#                      after concatenation.
#
# Note:
# Both DataFrames should generally have the same
# column names for meaningful results.
# ==================================================

print("-------------Vertical Concatenation---------------")
df_concat = pd.concat(
    [df_region1, df_region2],
    axis=0,
    ignore_index=True
)

print(df_concat)

# ==================================================
# Horizontal Concatenation
#
# Syntax:
# pd.concat([df1, df2],
#           axis=1)
#
# Parameters:
# axis=1 -> Combines DataFrames column-wise.
#
# Note:
# DataFrames should generally have the same number
# of rows. Columns from both DataFrames are placed
# side by side.
# ==================================================


print("-------------Horizontal Concatenation---------------")
df_concat = pd.concat(
    [df_region1, df_region2],
    axis=1,
    ignore_index=True
)

print(df_concat)