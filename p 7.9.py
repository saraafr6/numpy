#Check if the following matrices are orthogonal or not:

import numpy as np
#a)
a=np.array([[-1,0,1],[0,1,0],[0,0,-1]])
aT=a.T
result=np.dot(aT,a)
print(result)
I=np.eye(3)
print(I)
if np.allclose(result, I):
     print("yes")
else:
     print("No")

#b)
b=np.array([[1,-1,1],[1,-1,-1],[0,1,0]])
bT=b.T
result=np.dot(bT,b)
print(result)
I=np.eye(3)
print(I)
if np.allclose(result, I):
     print("yes")
else:
     print("No")


#c)
c=np.array([[0,0,0,1],[0,0,1,0],[1,0,0,0],[0,1,0,0]])
cT=c.T
result=np.dot(cT,c)
print(result)
I=np.eye(4)
print(I)
if np.allclose(result, I):
     print("yes")
else:
     print("No")
