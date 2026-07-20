# ==================================================
# Merge DataFrames
#
# Syntax:
# pd.merge(df1, df2,
#          on='Common_Column',
#          how='Join_Type')
#
# Merge combines two DataFrames based on a common
# column, similar to SQL JOIN.
# ==================================================

import pandas as pd

df_customer = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Ramesh", "Suresh", "Dinesh"]
})

df_order = pd.DataFrame({
    "CustomerID": [1, 2, 5],
    "OrderAmount": [250, 450, 350]
})

# ==================================================
# Inner Join
#
# Returns only the rows that have matching values
# in both DataFrames.
# ==================================================

print("Inner Join")

df_merge = pd.merge(
    df_customer,
    df_order,
    on="CustomerID",
    how="inner"
)

print(df_merge)

# ==================================================
# Outer Join
#
# Returns all rows from both DataFrames.
# Non-matching values are filled with NaN.
# ==================================================

df_merge = pd.merge(
    df_customer,
    df_order,
    on="CustomerID",
    how="outer"
)

print("\n\nOuter Join\n", df_merge)

# ==================================================
# Left Join
#
# Returns all rows from the left DataFrame
# (df_customer) and matching rows from the
# right DataFrame.
# ==================================================

df_merge = pd.merge(
    df_customer,
    df_order,
    on="CustomerID",
    how="left"
)

print("\n\nLeft Join\n", df_merge)

# ==================================================
# Right Join
#
# Returns all rows from the right DataFrame
# (df_order) and matching rows from the
# left DataFrame.
# ==================================================

df_merge = pd.merge(
    df_customer,
    df_order,
    on="CustomerID",
    how="right"
)

print("\n\nRight Join\n", df_merge)

# ==================================================
# Cross Join
#
# Returns the Cartesian Product of both DataFrames.
# Every row of the first DataFrame is combined with
# every row of the second DataFrame.
#
# Syntax:
# pd.merge(df1, df2, how='cross')
# ==================================================

# df_merge = pd.merge(df_customer, df_order, how="cross")
# print("\n\nCross Join\n", df_merge)