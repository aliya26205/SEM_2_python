import pandas as pd
df1=pd.DataFrame({
    "city":["Manglore","Banglore","Mysore"],
    "temp":[32,45,67]
})
print("Data frame 1:\n",df1)
df2=pd.DataFrame({
    "city":["Manglore","Banglore","Mysore"],
    "humid":[32,45,67]
})
print("Data frame 1:\n",df2)
df1['wind']=[20,30,40]
print("Data frame 1:\n",df1)
df1=pd.merge(df1,df2,on='city')
print(df1)
