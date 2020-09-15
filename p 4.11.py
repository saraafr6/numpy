#Compute the following product of three matrices:
import numpy as np
a=np.array([[2,10,-5,0],[0,0,1,3]])
b=np.array([[1,3],[0,2],[5,1],[-3,-4]])
c=np.array([[1,1],[1,1]])
print(np.dot(np.dot(a,b),c))
