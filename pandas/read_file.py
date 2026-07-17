import pandas as pd

# ============================================================
# READING FILES USING PANDAS
# ============================================================

# ------------------------------------------------------------
# 1. Read a CSV (Comma Separated Values) File
# Syntax:
# pd.read_csv("file_path")
# ------------------------------------------------------------
df = pd.read_csv("Data/teachers.csv")

# Display the DataFrame
print(df)


# ------------------------------------------------------------
# 2. Read a JSON File
# Syntax:
# pd.read_json("file_path")
# ------------------------------------------------------------
df = pd.read_json("Data/sample_Data.json")

# Display the DataFrame
print(df)


# ------------------------------------------------------------
# 3. Read an Excel File (.xlsx)
# Syntax:
# pd.read_excel("file_path")
# ------------------------------------------------------------
df = pd.read_excel("Data/SampleSuperstore.xlsx")

# Display the DataFrame
print(df)


# ============================================================
# COMMON PARAMETERS FOR READING FILES
# ============================================================

# ------------------------------------------------------------
# Encoding
# Used when a file contains special characters or when
# UnicodeDecodeError occurs.
#
# Common encodings:
# utf-8      -> Default encoding
# latin1     -> Latin-1 encoding
# cp1252     -> Windows encoding
# iso-8859-1 -> Older Latin encoding
# ------------------------------------------------------------

# df = pd.read_csv("Data/teachers.csv", encoding="utf-8")
# df = pd.read_csv("Data/teachers.csv", encoding="latin1")
# df = pd.read_csv("Data/teachers.csv", encoding="cp1252")


# ------------------------------------------------------------
# Read only the first N rows
# Useful for very large datasets.
# ------------------------------------------------------------

# df = pd.read_csv("Data/teachers.csv", nrows=100)


# ------------------------------------------------------------
# Read only selected columns
# Saves memory and improves performance.
# ------------------------------------------------------------

# df = pd.read_csv(
#     "Data/teachers.csv",
#     usecols=["Name", "Age", "Salary"]
# )


# ------------------------------------------------------------
# Skip rows while reading
# ------------------------------------------------------------

# df = pd.read_csv("Data/teachers.csv", skiprows=5)


# ------------------------------------------------------------
# Read without a header row
# ------------------------------------------------------------

# df = pd.read_csv("Data/teachers.csv", header=None)


# ------------------------------------------------------------
# Use a specific row as the header
# ------------------------------------------------------------

# df = pd.read_csv("Data/teachers.csv", header=2)


# ------------------------------------------------------------
# Specify a custom delimiter (separator)
# Default separator is comma (,)
# ------------------------------------------------------------

# Semicolon-separated file
# df = pd.read_csv("Data/teachers.csv", sep=";")

# Tab-separated file (.tsv)
# df = pd.read_csv("Data/teachers.tsv", sep="\t")


# ------------------------------------------------------------
# Read a large CSV file in chunks
# Loads small portions instead of the entire file.
# Best for datasets with millions of rows.
# ------------------------------------------------------------

# for chunk in pd.read_csv("Data/teachers.csv", chunksize=10000):
#     print(chunk)


# ------------------------------------------------------------
# Read a specific sheet from an Excel file
# ------------------------------------------------------------

# df = pd.read_excel(
#     "Data/SampleSuperstore.xlsx",
#     sheet_name="Orders"
# )


# ------------------------------------------------------------
# Read all sheets from an Excel file
# Returns a dictionary of DataFrames.
# ------------------------------------------------------------

# df = pd.read_excel(
#     "Data/SampleSuperstore.xlsx",
#     sheet_name=None
# )


# gcsfs