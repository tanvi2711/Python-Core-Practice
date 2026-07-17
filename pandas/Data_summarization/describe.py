import pandas as pd

# ============================================================
# describe() in Pandas
# Returns descriptive statistics of numerical columns.
# It provides a quick statistical summary of the dataset.
# ============================================================

# Create a dictionary
data = {
    'Name': ['Ramesh', 'Suresh', 'Jayesh', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    'Age': [50, 49, 23, 54, 56, 34, 37, 48],
    'Salary': [45000, 30000, 200000, 70000, 43000, 29000, 43000, 20000],
    'Performance_Score': [89, 50, 65, 76, 98, 87, 78, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

print("------------ Employee Data ---------------")
print(df)

print("----------- Descriptive Statistics -----------")
print(df.describe())

# describe() displays descriptive statistics for numerical columns:
# - count : Total number of non-missing (non-null) values
# - mean  : Arithmetic average of the values
# - std   : Standard deviation (measures how much the values are spread
#           around the mean; higher std = more variation)
# - min   : Smallest value in the column
# - 25%   : First Quartile (Q1) - 25% of the values are less than or equal to this value
# - 50%   : Second Quartile (Q2) / Median - 50% of the values are below and 50% are above this value
# - 75%   : Third Quartile (Q3) - 75% of the values are less than or equal to this value
# - max   : Largest value in the column
