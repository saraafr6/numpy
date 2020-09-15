#Given a , find a10

#a**10=Q A10 invQ
import numpy as np
a=np.array([[2,2],[5,-1]])
values,vectors=np.linalg.eig(a)
A=np.array([[values[0],0],[0,values[1]]])
A10=np.array([[A[0][0]**10,0],[0,A[1][1]**10]])
Q=vectors
#print("A is \n{} \n  Q is \n{}".format(A,Q))
invQ=np.linalg.inv(Q)
x=np.dot(Q,A10)
y=np.dot(x,invQ)
print("a**10 =",y)
