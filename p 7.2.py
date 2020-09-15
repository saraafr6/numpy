#Compute the eigenvalues of the matrix a
import numpy as np
a=np.array([[1,1],[1,0]])
values,vectors=np.linalg.eig(a)
print(values)
