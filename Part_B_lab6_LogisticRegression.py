import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("User_Data.csv")
print(df.head())
df['Gender']=df['Gender'].map({ "Male":1 , "Female":0})
print(df.head())

x=df[['Gender','Age','EstimatedSalary']]
y=df['Purchased']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
print("testing:\n",x_test[:5])
print("trinibg:\n",x_train[:5])

model=LogisticRegression()
model.fit(x_train,y_train)
y_predict=model.predict(x_test)
print("Actual value:\n",y_test.values)
print("Predicted values:\n",y_predict)

cm=confusion_matrix(y_test,y_predict)
ac=accuracy_score(y_test,y_predict)
print("Confusion matrix:\n",cm)
print("Accuracy score:\n",ac)

sns.heatmap(cm,fmt="d",annot=True,cmap="Reds")
plt.title("Confusion Matrix:")
plt.xlabel("Predicted values")
plt.ylabel("Actual values")
plt.show()
