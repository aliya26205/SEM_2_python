import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("AAPL.csv",parse_dates=True,index_col="Date")
print(df.head())

df['20_MA']=df['Close'].rolling(window=20).mean()
plt.figure(figsize=(10,5))
plt.plot(df['Close'],label="Close",color="red")
plt.plot(df['20_MA'],label="20_ma",color="blue")
plt.grid()
plt.show()

monthly_avg=df['Close'].resample("ME").mean()
plt.figure(figsize=(10,5))
plt.plot(monthly_avg,color="orange")
plt.grid()
plt.show()
