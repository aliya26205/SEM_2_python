#part-b lab 2 (b)
import numpy as np
import matplotlib.pyplot as plt
arr=np.array([1,2,3,4,5])
print("Orginal array:\n",arr)
print("Adding 5 to array:\n",arr+5)
print("Multiply 5 to array:\n",arr*5)

x=np.linspace(0,2*np.pi,100)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.plot(x,y_sin,label="sin")
plt.plot(x,y_cos,label="cos")
plt.xlabel("X value")
plt.ylabel("Y value")
plt.title("Sin and Cost")
plt.legend()
plt.show()
