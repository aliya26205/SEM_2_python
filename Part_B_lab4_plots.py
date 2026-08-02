import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y,label="line")
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y label")
plt.legend()
plt.show()

cat=['A','B','C','D','F']
val=[2,4,6,8,10]
plt.bar(cat,val)
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y label")
plt.show()

slices=[20,30,25,25]
label=['A','B','C','D']
plt.pie(slices,labels=label)
plt.title("Pie Chart")
plt.show()

x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.scatter(x,y,label="scatter")
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y label")
plt.legend()
plt.show()

data=[1,2,2,3,3,3,4,4,5]
plt.hist(data,bins=5)
plt.title("Histogram")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.show()
