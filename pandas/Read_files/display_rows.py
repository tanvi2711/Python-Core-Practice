# ============================================================
# head() and tail() in Pandas
# head() -> Returns the first n rows.
# tail() -> Returns the last n rows.
# Default value for n is 5.
# ============================================================

import pandas as pd

# Read the CSV file
df = pd.read_csv("DataSets/teachers.csv")

# Display the first 10 rows
print("Display 1st 10 rows")
print(df.head(10))

# Negative value: Excludes the last row and displays the remaining rows
print(df.head(-1))

# Display the last 10 rows
print("Display last 10 rows")
print(df.tail(10))

# Negative value: Skips the first 25 rows and displays the remaining rows
print(df.tail(-25))