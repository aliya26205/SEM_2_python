#Single Linear Regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as py
df=pd.read_csv("student_scores.csv")
print(df.head())
hours=df['Hours'].values.reshape(-1,1)
scores=df['Scores'].values.reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(hours,scores,test_size=0.2,random_state=0)

model=LinearRegression()
model.fit(x_train,y_train)
r_seq=model.score(x_train,y_train)
intercept=model.intercept_.item()
slop=model.coef_.item()
print(f"R^2:{r_seq:.2f}")
print(f"intercept:{intercept:.2f}")
print(f"Slop:{slop:.2f}")

y_pred=model.predict(x_test)
print("Actual score:\n",y_test)
print("Pridcited score:\n",y_pred)
new_hr=np.array([[5.2]])
p_s=model.predict(new_hr).item()
print("Predict value for 5.2 hr is:",p_s)

plt.plot(x_train,model.predict(x_train),color="red")
plt.scatter(hours,scores,color="green")
plt.title("Single linear Regression")
plt.legend(["predict line","Actual data"])
plt.xlabel("Hourse")
plt.ylabel("scores")
plt.show()
