#Find the matrix X
# x is inv(Q)
import numpy as np
a=np.array([[1,1],[1,0]])
values,vec=np.linalg.eig(a)
phi=values[0]
Q=np.array([[1,1],[1/phi,-phi]])
#print(Q)
x=np.linalg.inv(Q)
print(x)
