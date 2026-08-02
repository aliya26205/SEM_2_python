import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("iris")
print(df)

sns.scatterplot(df,x="sepal_length",y="sepal_width",hue="species")
plt.title("sepal_length VS sepal_width")
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.legend()
plt.show()

sns.boxplot(df,x="species",y="petal_width",hue="species")
plt.title("Species VS  petal_width")
plt.xlabel("Species")
plt.ylabel("petal_width")
plt.show()

sns.histplot(df["sepal_length"],kde=True)
plt.title("Distribution of petel length")
plt.xlabel("Petal length")
plt.show()
