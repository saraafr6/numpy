#Find eigenvalues for the matrices below:

#a)
import numpy as np
a=np.array([[4,2],[0,5]])
values,vectors=np.linalg.eig(a)
print("a: " ,values)

#b)
b=np.array([[3,1],[1,2]])
values,vectors=np.linalg.eig(b)
print("b: ",values)
           

#c)
c=np.array([[2,0,1],[1,2,0],[0,4,-1]])
values,vectors=np.linalg.eig(c)
print("c: ",values)

#d)
d=np.array([[-3,0,0],[4,1,0],[2,1,-1]])
values,vectors=np.linalg.eig(d)
print("d: ",values)
