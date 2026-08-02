#Multiple Linear Regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
df=pd.read_csv("Real_estate.csv")
print(df.columns)
df.drop('No',axis=1,inplace=True)
df.drop('X1 transaction date',axis=1,inplace=True)
print(df.columns)

x=df.drop('Y house price of unit area',axis=1)
y=df['Y house price of unit area']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)

model=LinearRegression()
model.fit(x_train,y_train)
r_seq=model.score(x_train,y_train)
intercept=model.intercept_
slop=model.coef_
print(f"R^2:{r_seq:.2f}")
print(f"intercept:{intercept:.2f}")
print(f"Slop:{slop:}")

y_predict=model.predict(x_test)
print("Actual value:\n",y_test.values)
print("Predicted value:\n",y_predict)

mae=mean_absolute_error(y_test,y_predict)
mse=mean_squared_error(y_test,y_predict)
print("MAE:",mae)
print("MSE:",mse)
