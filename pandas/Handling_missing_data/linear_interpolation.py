import pandas as pd

data = {
    "Time": [1, 2, 3, 4, 5],
    "Value": [10, None, 30, None, 50]
}

df = pd.DataFrame(data)

print("Before Interpolation")
print(df)

# ==================================================
# Linear Interpolation
#
# Syntax:
# df['Column_Name'] = df['Column_Name'].interpolate(method='linear')
#
# method='linear' estimates missing values using
# the nearest previous and next numeric values.
#
# Formula (for one missing value between two values):
# Estimated Value = (Previous Value + Next Value) / 2
# ==================================================

# Time = 2
# (10 + 30) / 2 = 20

# Time = 4
# (30 + 50) / 2 = 40

# Fill missing values in the Value column
df["Value"] = df["Value"].interpolate(method='linear')

print("\nAfter Interpolation")
print(df)


