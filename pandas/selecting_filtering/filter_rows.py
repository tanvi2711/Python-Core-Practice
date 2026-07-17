import pandas as pd

# Sample employee dataset
data = {
    'Name': ['Ramesh', 'Suresh', 'Jayesh', 'Dhiraj', 'Mangesh', 'Ritu', 'Shamika', 'Simran'],
    'Age': [50, 49, 23, 54, 56, 34, 37, 48],
    'Salary': [45000, 30000, 200000, 70000, 43000, 29000, 43000, 20000],
    'Performance_Score': [89, 50, 65, 76, 98, 87, 78, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

print("Sample Data")
print(df)


# ============================================================
# Filter Rows Using a Single Condition
# Returns rows where Salary is greater than 50,000.
# Syntax: df[df["column"] > value]
# ============================================================

high_salary = df[df["Salary"] > 50000]

print("\n\nEmployees with Salary > 50000")
print(high_salary)


# ============================================================
# Filter Rows Using Multiple Conditions (AND)
# '&' returns rows where ALL conditions are True.
# Each condition must be enclosed in parentheses.
# ============================================================

filtered = df[(df["Age"] > 36) & (df["Salary"] > 20000)]

print("\n\nEmployees with Age > 36 AND Salary > 20000")
print(filtered)


# ============================================================
# Filter Rows Using Multiple Conditions (OR)
# '|' returns rows where ANY one condition is True.
# Each condition must be enclosed in parentheses.
# ============================================================

filtered_or = df[(df["Age"] > 36) | (df["Performance_Score"] > 90)]

print("\n\nEmployees with Age > 36 OR Performance Score > 90")
print(filtered_or)