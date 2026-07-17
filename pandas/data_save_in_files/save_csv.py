import pandas as pd 

data={
    'Name':['Ram','Shyam','Jay'],
    'Age':[10,20,30],
    'City':['Nagpur','Mumbai','Pune']
}

df=pd.DataFrame(data)
print(df)

df.to_csv("output.csv",index=False)