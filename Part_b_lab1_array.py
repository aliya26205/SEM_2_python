import numpy as np
m=int(input("Enter no of rows:"))
n=int(input("Enter np of columns:"))
a=np.empty((m,n),dtype=int)
print("Enter",m*n," Matrix Array elemts:")
for i in range(m):
    for j in range(n):
        a[i][j]=int(input(f"Enter the element at position [{i}{j}]:"))

print("Array:")
print(a)
print("Array attributes")
print("Shape:",a.shape)
print("Dimention:",a.ndim)
print("Size:",a.size)
print("Total size",a.itemsize,"Bytes")
print("Total memeory:",a.nbytes,"Bytes")
