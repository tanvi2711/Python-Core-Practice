# head() and tail()

import pandas as pd 

df=pd.read_csv("DataSets/teachers.csv")
print(df.head(6))
print(df.head(-1))

print(df.tail(3))