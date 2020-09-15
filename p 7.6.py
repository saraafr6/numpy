#Compute the eigenvalues and eigenvectors of these matrices:

import numpy as np
#a)
a=np.array([[0,1],[1,0]])
values,vectors=np.linalg.eig(a)
print("a values: ",values)
print("a vectore: \n",vectors)
#b)
b=np.array([[0,1,0],[0,0,1],[-6,-1,4]])
values,vectors=np.linalg.eig(b)
print("b values: ",values)
print("b vectore: \n",vectors)
